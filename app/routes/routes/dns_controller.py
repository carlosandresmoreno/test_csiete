from concurrent.futures import thread
from importlib.resources import path
from typing import List
from fastapi import APIRouter
from fastapi import Depends

#utils
import threading

#schemes
from schemes.dns import DnsBase, ResponseDns, ResponseDnsTypes
from models.models import DnsType
#config
from config.db_connection import get_db, Session
#services
from services.index import CrudDns, DnService
#utilities
from utilities.dns_scan import Read_DNS

dns = APIRouter(tags=["CRUD_DNS"])

dn_service = DnService(0)

@dns.get(
    path ='/read_dns',
    response_description = 'Get Succesfully',
    response_model = List[ResponseDns]
)

async def read_dns(db_connection:Session = Depends(get_db)):

    result = await CrudDns.read_dns(db_connection)
    return result

@dns.get(
    path ='/run_verification_dns',
    response_description = 'Get Succesfully'
)
def DNS_verification(db_connection:Session = Depends(get_db)):
    ##DnService.run_verification(db_connection)
    dn_service.run = threading.Thread(
        target = dn_service.run_verification,
        args = (db_connection,)
        )
    dn_service.run.start()
    return {'message': 'running process'}

@dns.get(
    path ='/get_status',
    response_description = 'Get Succesfully'
)
def get_status(db_connection:Session = Depends(get_db)):
    ##DnService.run_verification(db_connection)

    return {'stop': dn_service.stop, 'thread_status': dn_service.run.is_alive() }

@dns.post(
    path ='/change_status',
    response_description = 'Get Succesfully'
)
def change_status(data: int ,db_connection:Session = Depends(get_db)):
    ##DnService.run_verification(db_connection)
    dn_service.stop = data

@dns.post(
    path ='/create_dns',
    response_description = 'Created Succesfully',
    response_model = ResponseDns
)

async def create_dns(data: DnsBase, db_connection:Session = Depends(get_db)):
    return await CrudDns.create_dns(db_connection,data)



@dns.get(
    path ='/get_type_dns',
    response_description = 'Get Succesfully',
    response_model = List[ResponseDnsTypes]
)
async def get_type_dns(db_connection:Session = Depends(get_db)):

    result = await CrudDns.get_DNS_types(db_connection)
    return result
