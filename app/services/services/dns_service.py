# utils
from threading import Thread
import time
from datetime import datetime
import dns
import dns.resolver
import logging

# fastapi httpException
from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy import true

# config
from config.db_connection import Session

# models
from models import models

# schemas
from schemes.dns import DnsBase, ResponseDns, ResponseDnsTypes
from schemes.logs import SystemLog

# other service
from .logs_service import CrudLog


logging.basicConfig(
    filename="logs_API.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)


class CrudDns:
    async def create_dns(db_connection: Session, dns: DnsBase):
        """create a DNS in database

        Args:
            db_connection (Session): db connection instance
            dns (DnsBase): data domain

        Raises:
            HTTPException: if there is an error creating the domain

        Returns:
            ResponseDns: the new data dns
        """
        db_dns = models.DNS(**dns.__dict__)
        try:
            db_connection.add(db_dns)
            db_connection.commit()
            db_connection.refresh(db_dns)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error creating DNS in database (connection error)",
            )

        del db_dns._sa_instance_state
        return ResponseDns(**db_dns.__dict__)

    def update_dns(db_connection: Session, name_DNS, index):
        """Update a DNS in database

        Args:
            db_connection (Session): db connection instance
            dns_body (DnsBase): data domain

        Raises:
            HTTPException: if there is an error creating the domain

        Returns:
            ResponseDns: the new data dns
        """
        try:
            db_DNS = (
                db_connection.query(models.DNS)
                .filter(
                    models.DNS.id_dns == index,
                )
                .first()
            )
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error getting comment from database (connection error)",
            )

        if db_DNS is not None:
            try:
                db_DNS.nombre_dns = name_DNS
                db_connection.commit()
                db_connection.refresh(db_DNS)
            except Exception as e:
                print(e)
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Error updating DNS name from database (connection error)",
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The DNS name with the specified id_dns not found",
            )
        del db_DNS._sa_instance_state
        return ResponseDns(**db_DNS.__dict__)

    async def get_DNS_types(db_connection: Session):
        result = db_connection.query(models.DnsType).all()
        li = []
        for a in result:
            li.append(a)
        return li

    async def read_dns(db_connection: Session):
        result = db_connection.query(models.DNS).all()
        li = []
        for a in result:
            li.append(a)
        return li

    async def DNS_verification(db_connection: Session):

        currents_DNS = await CrudDns.read_dns(db_connection)
        return currents_DNS


class DnService:
    def __init__(self, stop: int):
        self.stop = stop

    def run_verification(self, db_connection: Session):
        self.stop = 1
        while True:
            time.sleep(60)
            domains = db_connection.query(models.Domains).all()
            type_dns = db_connection.query(models.DnsType).all()

            for domain in domains:
                dns_by_domain = domain.dns

                for i_dns, i_dns_by_domain in zip(type_dns, dns_by_domain):
                    try:
                        ans = dns.resolver.resolve(domain.nombre_dominio, i_dns.nombre)
                        name = str(ans[0])
                    except:
                        name = ""

                    if name == i_dns_by_domain.nombre_dns:
                        print("son iguales!!!")
                    else:
                        db_logs = f"""In {domain.nombre_dominio} domain there was a DNS change: DNS Type: {i_dns.nombre}, 
                            Old DNS: {i_dns_by_domain.nombre_dns}, Current DNS: {name}"""
                        logging.info(db_logs)
                        new_log = SystemLog(
                            id_dns=i_dns_by_domain.id_dns,
                            description=db_logs,
                            date=datetime.now(),
                        )

                        try:
                            CrudLog.create_log(new_log, db_connection)
                            CrudDns.update_dns(
                                db_connection, name, i_dns_by_domain.id_dns
                            )
                        except Exception as e:
                            print(e)
            print('completed process!!')

            if self.stop == 0:
                break
        
