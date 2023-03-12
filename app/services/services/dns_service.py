# utils
from threading import Thread
import time
import dns
import dns.resolver
# fastapi httpException
from typing import List
from fastapi import HTTPException, status
from sqlalchemy import true


# config
from config.db_connection import Session

# models
from models import models

# schemas
from schemes.dns import DnsBase, ResponseDns, ResponseDnsTypes


class CrudDns:

    async def create_dns(db_connection: Session, dns: DnsBase):
        """create a DNS in database

        Args:
            db_connection (Session): db connection instance
            domain (DnsBase): data domain

        Raises:
            HTTPException: if there is an error creating the domain

        Returns:
            ResponseDns: the new data domain
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
        print("iniciando ciclo")
        while True:
            time.sleep(10)
            domains = db_connection.query(models.Domains).all()
            type_dns = db_connection.query(models.DnsType).all()

            print("==lista=====")
            print(type_dns)

            for domain in domains:
                print(domain.id_dominio)
                print(domain.nombre_dominio)
                dns_by_domain = domain.dns

                for i_dns, i_dns_by_domain in zip(type_dns, dns_by_domain):
                    print("resultado============>>")
                    try:
                        ans = dns.resolver.resolve(
                            domain.nombre_dominio, i_dns.nombre)
                        name = str(ans[0])
                    except:
                        name = "" 
                    
                    if name == i_dns_by_domain.nombre_dns:
                        print("son iguales!!!")
                        print(domain.nombre_dominio)
                        print(i_dns.nombre)
                        print(name)
                        print(i_dns_by_domain.nombre_dns)
                    else:
                        print("son diferentes!!!")
                        print(domain.nombre_dominio)
                        print(i_dns.nombre)
                        print(name)
                        print(i_dns_by_domain.nombre_dns)

            if self.stop == 0:
                break
        print("terminando ciclos")
