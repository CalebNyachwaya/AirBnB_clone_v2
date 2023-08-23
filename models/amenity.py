#!/usr/bin/python3
# amenity.py
"""
    module containing Amenity class
"""

from models.base_model import BaseModel, Base
from models.city import City
from os import environ
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
        Amenity class
    """

    if (storage_engine == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        from models.place import place_amenity
        place_amenities = relationship(
            "Place",
            secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
