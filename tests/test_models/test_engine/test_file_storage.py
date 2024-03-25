
from models.engine.file_storage import FileStorage
import unittest
import models
import os
from models.base_model import BaseModel
'''A module to test storage'''


class TestStorage(unittest.TestCase):
    '''Testing the storage operation'''

    def setUp(self):
        self.B1 = BaseModel()

    def test_new(self):
        B2 = BaseModel()
        self.assertIn("BaseModel." + B2.id, models.storage.all().keys())

    def test_FileStorage(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_save(self):
        B2 = BaseModel()
        models.storage.new()
        models.storage.save()
        txt = ""
        with open("file.json", "r") as f:
            txt = f.read()
        self.assertin("BaseModel." + B2.id, txt)


if __name__ == '__main__':
    unittest.main()
