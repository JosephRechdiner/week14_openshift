from fastapi import FastAPI
from routes.external_route import external_router

app = FastAPI()

app.include_router(external_router)