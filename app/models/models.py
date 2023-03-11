from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from config.db_connection import Base
from sqlalchemy.orm import relationship


class Domains(Base):
    __tablename__ = "dominios"

    id_dominio = Column(Integer, primary_key=True, autoincrement=True)
    nombre_dominio = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

class DnsType(Base):
    __tablename__ = "tipos_dns"
    
    id_tipo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    
class DNS(Base):
    __tablename__ = "DNS"

    id_dns = Column(Integer, primary_key=True, autoincrement=True)
    id_dominio = Column(Integer,ForeignKey("dominios.id_dominio"))  # Falta terminar modelitos 
    id_tipo = Column(Integer, ForeignKey("tipos_dns.id_tipo")) 
    nombre_dns = Column(String(255), nullable=False)
    
class SystemLogs(Base):
    __tablename__ = "system_logs"
    
    id_logs = Column(Integer, primary_key=True, autoincrement=True)
    id_dns = Column(Integer, ForeignKey("DNS.id_dns"))
    description = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)