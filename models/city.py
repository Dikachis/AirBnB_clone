#!/usr/bin/python3
""" Class City """

from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
