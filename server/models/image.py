from datetime import datetime


class Image:
    def __init__(self, name: str, path: str, extension: str, creation_date: datetime):
        self._original_name = name
        self._original_path = path
        self._name = name
        self._path = path
        self._extension = extension
        self._creation_date = creation_date

    def get_original_name(self):
        return self._original_name
    
    def get_original_path(self):
        return self._original_path
    
    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_extension(self):
        return self._extension

    def get_creation_date(self):
        return self._creation_date

    def get_name_with_extension(self):
        return self._name + self._extension

    def set_name(self, name):
        self._name = name

    def set_path(self, path):
        self._path = path

    def set_extension(self, extension):
        self._extension = extension

    def set_creation_date(self, data):
        self._creation_date = data
