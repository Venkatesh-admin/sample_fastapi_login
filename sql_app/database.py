# sql_app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from .models import User  # Import the User model

DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for declarative models
Base = declarative_base()

# Function to create a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables on startup
def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError as e:
        print(f"Error creating tables: {e}")
