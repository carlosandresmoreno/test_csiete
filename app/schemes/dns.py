from unittest.util import _MAX_LENGTH
from xmlrpc.client import boolean
from pydantic import BaseModel,Field

class DnsBase(BaseModel):
    id_tipo: int
    id_dominio:int
    nombre_dns:str = Field(max_length= 255)

class ResponseDns(DnsBase):
    id_dns:int
    id_dominio:int
    nombre_dns:str

class ResponseDnsTypes(BaseModel):
    id_tipo:int
    nombre:str = Field(max_length= 255)
    is_active:bool

    class Config:
        orm_mode = True
