from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base

DATABASE_URL = "sqlite:///db.sqlite3"

# Create the engine and session factory
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Initialize the database
def init_db():
    Base.metadata.create_all(engine)
