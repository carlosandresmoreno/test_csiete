# Prueba tecnica 

Esta es una prueba tecnica que se compone de una API desarrolada en FastAPI(Python) conectada
a una base de datos relacional

![diagrama del proyecto](/documentation/database_diagram.jpg)


## Correr el proyecto usando entorno virtuales

1 - Creacion del entorno virtual
```sh
    python3 venv -m venv venv
```
2 - Instalacion de requerimientos
```sh
    pip install -r requirements.txt
```
3 - Importacion de base de datos
```sh
    en la ruta ./db/ esta la base de datos llamada "bd", esta la importamos desde un gestor de bases de datos (workbench,dbdeaver)) y ya tendremos la base de datos con sus respectivas tablas
```
4 - Configuracion .env
```sh
    en la carpeta /app se encuentra el .envExample con los parametros que se deben diligenciar para la conexion con la base de datos
```
5 - Ejecucion de la API
```sh
    uvicorn app.manage:app --host=0.0.0.0 --port=4500 --reload
```

## Correr el proyecto usando Docker

Puedes correr la API y la base de datos de la siguiente manera en la raiz del proyecto:

1 - Configuracion .env
```sh
    en la carpeta /app se encuentra el .envExample con los parametros que se deben diligenciar para la conexion con la base de datos
```

2 - levantar API y Base de datos con docker Compose
```sh
    sudo docker-compose build
    sudo docker-compose up
```