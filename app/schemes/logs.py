from datetime import datetime
from pydantic import BaseModel, Field


class SystemLog(BaseModel):
    id_dns: int
    description: str = Field(max_length=255)
    date: datetime

class LogResponse(BaseModel):
    id_dns: int
    description: str = Field(max_length=255)
    date: datetime