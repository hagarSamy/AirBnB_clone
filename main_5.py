#!/usr/bin/python3
import os
from models.engine.file_storage import FileStorage

fs = FileStorage()
print(type(fs.save))
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass

try:    
    os.remove(file_path)
except:
    pass

fs.save()

print(os.path.exists(file_path))

try:
    os.remove(file_path)
except Exception as e:
    pass
