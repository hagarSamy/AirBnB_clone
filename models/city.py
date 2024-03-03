#!/usr/bin/python3
'''A module that handles the city'''

from models.base_model import BaseModel


class City(BaseModel):
    '''A class that inherits from BaseModel
    Args:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    '''

    state_id = ""
    name = ""
