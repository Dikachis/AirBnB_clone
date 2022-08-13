#!/usr/bin/python3
""" Class State """

from models.base_model import BaseModel


class State(BaseModel):
    """ Class State """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
