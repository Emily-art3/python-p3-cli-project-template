# lib/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the SQLite URL for the database
DATABASE_URL = "sqlite:///db.sqlite3"

# Create the engine, passing options if necessary (e.g., check_same_thread=False for SQLite)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create the sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the session for transactions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
