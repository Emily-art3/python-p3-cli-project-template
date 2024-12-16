from lib.db.models import User, Project
from lib.seed import session  # Import the session from seed.py

def create_user(name, email):
    """Add a new user to the database."""
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} added successfully!")

def list_users():
    """List all users in the database."""
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id} | Name: {user.name} | Email: {user.email}")

def create_project(user_id, title, description):
    """Add a new project for a specific user."""
    user = session.query(User).get(user_id)
    if user:
        project = Project(title=title, description=description, user_id=user_id)
        session.add(project)
        session.commit()
        print(f"Project '{title}' added successfully for user {user.name}!")
    else:
        print(f"User with ID {user_id} not found.")
