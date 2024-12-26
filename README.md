# My FastAPI App

This project is a FastAPI application that connects to a MySQL server. It serves as a template for building RESTful APIs with FastAPI, SQLAlchemy, and Alembic for database migrations.

## Project Structure

```
my-fastapi-app
├── app
│   ├── main.py                # Entry point of the FastAPI application
│   ├── api
│   │   └── v1
│   │       └── endpoints
│   │           └── example.py # API endpoints for the example resource
│   ├── core
│   │   └── config.py          # Configuration settings for the application
│   ├── db
│   │   ├── base.py            # Base class for SQLAlchemy models
│   │   ├── session.py         # Database session setup
│   │   └── models
│   │       └── example.py     # SQLAlchemy model for the example resource
│   └── schemas
│       └── example.py         # Pydantic schemas for data validation
├── alembic
│   ├── env.py                 # Alembic migration environment setup
│   ├── script.py.mako         # Template for migration scripts
│   └── versions               # Directory for migration scripts
├── alembic.ini                # Alembic configuration file
├── requirements.txt           # Project dependencies
├── Dockerfile                 # Docker image instructions
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-fastapi-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   Update the database connection details in `app/core/config.py`.

5. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

## Usage

Once the application is running, you can access the API at `http://localhost:8000`. The API documentation is available at `http://localhost:8000/docs`.

## Database Migrations

To manage database migrations, use Alembic commands. For example, to create a new migration:
```
alembic revision --autogenerate -m "Migration message"
```

To apply migrations:
```
alembic upgrade head
```

## License

This project is licensed under the MIT License.