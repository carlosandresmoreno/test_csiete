# fastapi httpException
from fastapi import HTTPException, status

# config
from config.db_connection import Session, get_db

# models
from models import models

# schemas
from schemes.domain import DomainBase,DomainResponse

#utilities
from utilities.dns_scan import Read_DNS

#other service
from .dns_service import CrudDns


class CrudDomain:

    async def verification_domain(db_connection, domain: DomainBase):
        try:
            list=[]
            query = db_connection.query(models.Domains).filter(
            models.Domains.nombre_dominio == domain.nombre_dominio
            )
            for q in query:
                list.append(q)
            
            if len(list) == 0:
                res = True
            else:
                res = False

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error deleting domain in database (connection error)",
                )
        return res




    async def create_domain(db_connection: Session, domain: DomainBase):
        """create a Domain in database

        Args:
            db_connection (Session): db connection instance
            domain (DomainBase): data domain

        Raises:
            HTTPException: if there is an error creating the domain

        Returns:
            DomainResponse: the new data domain
        """
        db_domain = models.Domains(**domain.__dict__)
        try:
            db_connection.add(db_domain)
            db_connection.commit()
            db_connection.refresh(db_domain)

            result_type_DNS = CrudDns.get_DNS_types(db_connection)
            read_DNS = Read_DNS.read_DNS(db_domain,result_create_DNS)
            result_create_DNS = await CrudDns.create_dns(db_connection,read_DNS)
            print(result_create_DNS)


        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error creating Domain in database (connection error)",
            )
        del db_domain._sa_instance_state
        
        return {'message':'Created successfully'}
        ##return DomainResponse(**db_domain.__dict__)
        


    
    async def delete_domain(db_connection: Session, id_domain: int):
            """to deleted domain in database

            Args:
                db_connection (Session): db connection instance
                id_domain (int): id of domain to delete

            Raises:
                HTTPException: Exception if a error occurs

            Returns:
                dict: message
            """
            try:
                db_connection.query(models.Domains).filter(
                    models.Domains.id_dominio == id_domain
                ).delete()
                db_connection.commit()
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Error deleting domain in database (connection error)",
                )
            return {"message": "deleted successfully"}
