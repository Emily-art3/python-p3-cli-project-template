# lib/helpers.py
from lib.db.database import SessionLocal
from lib.db.models import User, Project

def create_user(name, email):
    db = SessionLocal()  # Create a session
    try:
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)  # Get the user object with its updated ID
        print(f"User {name} created with ID: {user.id}")
    except Exception as e:
        db.rollback()
        print(f"Error creating user: {e}")
    finally:
        db.close()

def list_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return users
    finally:
        db.close()
