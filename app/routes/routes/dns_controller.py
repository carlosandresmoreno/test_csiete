from importlib.resources import path
from typing import List
from fastapi import APIRouter
from fastapi import Depends

#schemes
from schemes.dns import DnsBase, ResponseDns, ResponseDnsTypes
from models.models import DnsType
#config
from config.db_connection import get_db, Session
#services
from services.index import CrudDns

dns = APIRouter(tags=["CRUD_DNS"])


@dns.post(
    path ='/create_dns',
    response_description = 'Created Succesfully',
    response_model = ResponseDns
)

def create_dns(data: DnsBase, db_connection:Session = Depends(get_db)):
    return(CrudDns.create_dns(db_connection,data))



@dns.get(
    path ='/get_type_dns',
    response_description = 'Get Succesfully',
    response_model = List[ResponseDnsTypes]
)
async def get_type_dns(db_connection:Session = Depends(get_db)):

    result = await CrudDns.get_DNS_types(db_connection)
    print(result)
    print(type(result))

    # result = db_connection.query(DnsType).all()
    # print(result[0].nombre)
    return result
