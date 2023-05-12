#!/usr/bin/python3
"""class"""
from models.base_model import BaseModel


class User(BaseModel):
    """objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
