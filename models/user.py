#!/usr/bin/python3
# user.py
"""
    Module containing the User class
"""
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
        Represents the User class
    """
    if (storage_engine == 'db'):
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
