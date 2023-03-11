# fastapi httpException
from typing import List
from fastapi import HTTPException, status

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
        li =[]
        for a in result:
            li.append(a)
        return li






        


