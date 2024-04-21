#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """represents an amenity for a MYSQL database"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    places = relationship("Place", secondary="place_amenity",
                           backref="associated_amenities",
                           overlaps="place_amenities",
                           viewonly=False)
