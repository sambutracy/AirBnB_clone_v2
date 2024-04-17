#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
 if getenv("HBNB_YPE_STORAGE") == "db":
     from models.engine.db_storage import DBStorage
     stage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
