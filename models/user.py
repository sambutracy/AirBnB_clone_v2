#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ - "users"
    email = Column(string(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(sring(128))
    last_name = Column(string(128))
