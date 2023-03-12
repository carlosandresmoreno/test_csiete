"""
main to run all the microservices
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#routes
from routes.index import domain
from routes.index import dns
from routes.index import logs

# Principal fastapi instance
app = FastAPI(
    title="Microservices Test DNS",
    description= "Microservices to complete the test"
)

#routes
app.include_router(domain)
app.include_router(dns)
app.include_router(logs)

#system cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)