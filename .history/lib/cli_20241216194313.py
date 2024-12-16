from database import SessionLocal, init_db
from models import User, Project

# Initialize the database when the program runs
init_db()

# Function to create a new user
def create_user(name, email):
    """Add a new user to the database."""
    session = SessionLocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} added successfully!")
    session.close()

# Function to list all users
def list_users():
    """Display all users in the database."""
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id} | Name: {user.name} | Email: {user.email}")
    session.close()

# Function to create a new project
def create_project(user_id, title, description):
    """Add a new project for a specific user. Args:
        name (str): The name of the project.
        description (str): A description of the project.
        user_id (int): The ID of the user who owns the project."""
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        project = Project(title=title, description=description, user_id=user_id)
        session.add(project)
        session.commit()
        print(f"Project '{title}' added for user {user.name}!")
    else:
        print(f"No user found with ID {user_id}.")
    session.close()
