import os
import json
from datetime import datetime
from Status import Status

class MapFile:

    def __init__(self, path = './', name = 'map', extension = 'json'):
        self._path = path
        self._name = name
        self._extension = extension
        self._created_at = None
        self._updated_at = None
        self._message = None
        self._status = None
        self._items = None
        self._sync() if self._exists() and self._has_data() else self._create()

    def _exists(self):
        return os.path.isfile(self.get_full_path())
    
    def _has_data(self):
        return os.stat(self.get_full_path()).st_size != 0
    
    def _get_data(self):
        with open(self.get_full_path(), 'r') as map_file:
            return json.load(map_file)

    def _sync(self):
        with open(self.get_full_path(), 'r') as map_file:
            data = json.load(map_file)
            self._created_at = data['_created_at']
            self._updated_at = data['_updated_at']
            self._items = data['_items']
            self._status = data['_status']
            self._message = data['_message']

    def _create(self):
        with open(self.get_full_path(), 'w') as map_file:
            self._created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._items = []
            self._status = Status.NOT_STARTED
            self._message = None
            map_file.write(self.to_json())

    def _update(self):
        with open(self.get_full_path(), 'w') as map_file:
            self._updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            map_file.write(self.to_json())

    def to_json(self):
        return json.dumps(
            self,
            default = lambda o: o.__dict__, 
            sort_keys = True,
            indent = 4)

    def get_full_path(self):
        return self._path + self._name + '.' + self._extension
    
    def get_items(self):
        return self._items
    
    def get_status(self):
        return self._status
    
    def get_message(self):
        return self._message
    
    def set_message(self, message):
        self._message = message
        self._update()
    
    def insert(self, item):
        self._items.append(item)
        self._update()