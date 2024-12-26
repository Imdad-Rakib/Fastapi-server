from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/mydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_db_connection():
    try:
        with engine.connect() as connection:
            print("Database connection established successfully.")
    except OperationalError as e:
        print(f"Database connection failed: {e}")