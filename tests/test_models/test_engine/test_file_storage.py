
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
'''A module to test storage'''


class TestStorage(unittest.TestCase):
    '''Testing the storage operation'''

    def setUp(self):
        self.B1 = BaseModel()
    
if __name__ == '__main__':
    unittest.main()
