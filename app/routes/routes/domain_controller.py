from typing import Any
from fastapi import APIRouter
from fastapi import Depends

# schemes
from schemes.domain import DomainBase, DomainResponse

# config
from config.db_connection import get_db, Session

# services
from services.index import CrudDomain

domain = APIRouter(tags=["CRUD_DOMAIN"])


@domain.get(
    path="/get_domain",
    response_description="Get successfully",
    response_model=DomainResponse,
)
async def get_domain(data: int, db_connection: Session = Depends(get_db)):
    return await CrudDomain.get_domain(db_connection, data)


@domain.post(
    path="/create_domain",
    response_description="Created successfully",
    ##response_model = DomainResponse
)
async def create_domain(data: DomainBase, db_connection: Session = Depends(get_db)):
    verification = await CrudDomain.verification_domain(db_connection, data)

    if verification:
        result: any = await CrudDomain.create_domain(db_connection, data)
    else:
        result: any = {"message": "domain already exists"}
    return result


@domain.delete(path="/delete_domain", response_description="Deleted successfully")
async def delete_domain(data: int, db_connection: Session = Depends(get_db)):
    result = await CrudDomain.delete_domain(db_connection, data)
    return result
