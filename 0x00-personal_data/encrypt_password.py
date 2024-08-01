#!/usr/bin/env python3
"""Python Module for hashing and validating passwords using bcrypt"""
import bcrypt

def hash_password(password: str) -> bytes:
    """
    Function to hash a password using bcrypt.
    
    Args:
    - password (str): The password to hash.
    
    Returns:
    - bytes: The hashed password as a byte string.
    """
    # Encode the password to bytes
    encoded_psw = bytes(password, 'utf-8')
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed = bcrypt.hashpw(encoded_psw, salt)
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Function to validate a password against a hashed password using bcrypt.
    
    Args:
    - hashed_password (bytes): The hashed password.
    - password (str): The password to validate.
    
    Returns:
    - bool: True if the password is valid, False otherwise.
    """
    # Encode the password to bytes
    encoded_psw = bytes(password, 'utf-8')
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(encoded_psw, hashed_password)
