from sqlalchemy.orm import Session
from .db import User, Property

# Create operations
def create_user(db: Session, username: str, email: str, password: str, is_active: bool = True):
    db_user = User(username=username, email=email, password=password, is_active=is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_property(db: Session, title: str, description: str, owner_id: int):
    db_property = Property(title=title, description=description, owner_id=owner_id)
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

# Read operations
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_property(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()

# Update operations
def update_user(db: Session, user_id: int, username: str, email: str, password: str, is_active: bool):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = username
        db_user.email = email
        db_user.password = password
        db_user.is_active = is_active
        db.commit()
        db.refresh(db_user)
    return db_user

def update_property(db: Session, property_id: int, title: str, description: str):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if db_property:
        db_property.title = title
        db_property.description = description
        db.commit()
        db.refresh(db_property)
    return db_property

# Delete operations
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def delete_property(db: Session, property_id: int):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if db_property:
        db.delete(db_property)
        db.commit()
    return db_property