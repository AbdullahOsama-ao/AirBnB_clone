#!/usr/bin/python3


"""
    __init__ Module for AirBnB clone
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
