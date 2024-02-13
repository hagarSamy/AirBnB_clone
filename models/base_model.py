#!/usr/bin/python3
'''A module containign the base class
from which all other classes will inherit'''

import uuid
from datetime import datetime


class BaseModel:
    '''The baseModel class'''

    def __init__(self, *args, **kwargs):
        '''Initiation of the base class
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        '''Upadtes updated_at to current date time'''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary'''

        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return (self.__dict__)

    def __str__(self):
        '''Beautifying the printed output'''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
