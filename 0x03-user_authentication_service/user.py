#!/usr/bin/env python3
"""
Module User
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a base class for declarative class definitions
Base = declarative_base()


class User(Base):
    """ Definition of class User
    SQLAlchemy model User

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'users'

    # Define columns in the 'users' table
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    # Non-nullable string column for hashed password
    hashed_password = Column(String(250), nullable=False)
    # Nullable string column for session ID
    session_id = Column(String(250))
    # Nullable string column for reset token
    reset_token = Column(String(250))
