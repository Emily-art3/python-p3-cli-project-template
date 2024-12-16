from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Step 1: User Table
class User(Base):
    __tablename__ = "users"  # Table name in the database
    id = Column(Integer, primary_key=True)  # Primary Key
    name = Column(String, nullable=False)  # User's name
    email = Column(String, unique=True, nullable=False)  # User's email
    projects = relationship("Project", back_populates="user")  # Relationship to projects

# Step 2: Project Table
class Project(Base):
    __tablename__ = "projects"  # Table name
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)  # Project title
    description = Column(Text)  # Description of the project
    user_id = Column(Integer, ForeignKey("users.id"))  # Link to the User table
    user = relationship("User", back_populates="projects")  # Back-reference to User
