import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

# Existing imports
from models.engine.db_storage import DBStorage

# Move this line to the bottom
storage = DBStorage()
storage.reload()

