
from models.engine.file_storage import FileStorage
import unittest
import models
from models.base_model import BaseModel
'''A module to test storage'''


class TestStorage(unittest.TestCase):
    '''Testing the storage operation'''

    def setUp(self):
        self.B1 = BaseModel()
    def test_new(self):
        B2 = BaseModel()
        self.assertIn("BaseModel." + B2.id, models.storage.all().keys())
    
if __name__ == '__main__':
    unittest.main()
