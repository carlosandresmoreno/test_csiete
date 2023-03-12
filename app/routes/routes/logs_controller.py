import imp
from fastapi import APIRouter
from fastapi import Depends

# config
from config.db_connection import get_db, Session

logs = APIRouter(tags=["CRUD_LOGS"])

# schemes
from schemes.logs import SystemLog, LogResponse

# model
from models.models import SystemLogs

# services
from services.index import CrudLog


@logs.get(path="/get_logs", response_description="Get Succesfully")
def get_logs(db_connection: Session = Depends(get_db)):
    return CrudLog.get_log(db_connection)


@logs.post(path="/create_logs", response_description="Create Succesfully")
def post_logs(data: SystemLog, db_connection: Session = Depends(get_db)):
    return CrudLog.create_log(data, db_connection)
