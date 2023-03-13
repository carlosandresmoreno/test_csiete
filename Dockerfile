FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY /app/requirements.txt /app/requirements.txt

WORKDIR /app
RUN python -m pip install -r requirements.txt


COPY ./app /app

EXPOSE 4500

CMD ["uvicorn","manage:app","--host=0.0.0.0","--port=4500","--reload"]

