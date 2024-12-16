from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Step 1: Create the Base class for defining models
Base = declarative_base()

# Step 2: Define the database engine (SQLite in this example)
engine = create_engine("sqlite:///phase3_project.db")

# Step 3: Create a session to interact with the database
SessionLocal = sessionmaker(bind=engine)

# Step 4: Function to initialize the database
def init_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(bind=engine)
