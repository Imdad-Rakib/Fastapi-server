from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "My FastAPI Project"
    VERSION: str = "1.0.0"
    SQLALCHEMY_DATABASE_URL: str = "mysql+mysqlconnector://ubuntu:123456@localhost:3306/mydb"

settings = Settings()