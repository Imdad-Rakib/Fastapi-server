from fastapi import FastAPI
# from app.api.v1.endpoints.example import router as example_router
from app.core.config import settings
from app.db.session import test_db_connection

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


test_db_connection()
# app.include_router(example_router, prefix="/api/v1/examples", tags=["examples"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}