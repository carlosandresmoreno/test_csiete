from pydantic import BaseModel, Field

class DomainBase(BaseModel):
    nombre_dominio: str = Field(max_length=255)
    
class DomainResponse(DomainBase):
    id_dominio: int
    is_active: bool