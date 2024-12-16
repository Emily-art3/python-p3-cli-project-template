from lib.db.database import engine
from lib.db.models import Base

# Create all tables in the database
Base.metadata.create_all(engine)
print("Database tables created successfully!")
