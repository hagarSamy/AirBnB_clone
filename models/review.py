#!/usr/bin/python3
'''A module that handles the review'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''A class that inherits from BaseModel
    Args:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    '''

    place_id = ""
    user_id = ""
    text = ""
