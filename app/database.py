from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Creates 'sqlite.db' file in your project folder automatically
DATABASE_URL = "sqlite:///./sqlite.db"

# SQLite requires 'check_same_thread=False' to allow FastAPI's multithreading
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory for handling database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for database tables
class Base(DeclarativeBase):
    pass

# Dependency to inject DB sessions into API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

