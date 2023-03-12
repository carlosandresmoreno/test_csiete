# fastapi httpException
from fastapi import Depends, HTTPException, status

# config
from config.db_connection import Session, get_db

# models
from models import models

# schemas
from schemes.logs import SystemLog, LogResponse


class CrudLog:
    def get_log(db_connection):
        """get a log in database

        Args:
            db_connection (Session): db connection instance

        Raises:
            HTTPException: if there is an error get the domain

        Returns:
            LogResponse: the new data domain
        """

        return db_connection.query(models.SystemLogs).all()

    def create_log(data: SystemLog, db_connection: Session = Depends(get_db)):
        """create a log in database

        Args:
            db_connection (Session): db connection instance
            data: data: SystemLog scheme

        Raises:
            HTTPException: if there is an error get the domain

        Returns:
            message: the new data domain
        """
        db_logs = models.SystemLogs(**data.__dict__)
        try:
            db_connection.add(db_logs)
            db_connection.commit()
            db_connection.refresh(db_logs)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error creating Domain in database (connection error)",
            )
        del db_logs._sa_instance_state
        return {"message": "Created successfully"}
