#!/usr/bin/env python3
"""
Module auth
"""
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4
from typing import Union

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Returns a salted hash of
    the input password
    """
    hashed_password = hashpw(password.encode('utf-8'), gensalt())

    return hashed_password