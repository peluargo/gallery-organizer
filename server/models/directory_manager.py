import os
from PIL import Image
from File import File

class DirectoryManager:
    def __init__(self):
        pass

    def create_file(self, file_path: str, content: str = ''):
        with open(file_path, 'x') as file:
            file.write(content)

    def read_file(self, file_path: str):
        with open(file_path, 'r') as file:
            return file.read()

    def override_file(self, file_path: str, content: str):
        with open(file_path, 'w') as file:
            file.write(content)

    def append_in_file(self, file_path: str, content: str):
        with open(file_path, 'a') as file:
            file.write(content + '\n')

    def is_file(self, path):
        return os.path.isfile(path)

    def file_exists(self, file_path: str):
        return os.path.isfile(file_path)
    
    def delete_file(self, file_path: str):
        os.remove(file_path)

    def create_folder(self, folder_path: str):
        os.mkdir(folder_path)

    def folder_exists(self, folder_path: str):
        return os.path.isdir(folder_path)

    def is_folder(self, path):
        return os.path.isdir(path)

    def create_folder_if_not_exist(self, folder_path: str):
        if not self.folder_exists(folder_path):
            os.mkdir(folder_path)

    def get_files_in_folder(self, folder_path: str):
        return [item for item in os.listdir(folder_path) if self.is_file(os.path.join(folder_path, item))]
    
    def get_file_data(self, file_path):
        file_data = Image.open(file_path).getexif()
        print(file_data)
        return file_data
    
    # def get_file_extension(self, file_path):
    #     file_extension = 
    
    def get_file_creation_date(self, file_path):
        file_data = self.get_file_data(file_path)
        file_creation_date = file_data.get(306)
        return file_creation_date

    def get_file_extension(self, file_path):
        file_extension = os.path.splitext(file_path)[1]
        return file_extension

# dm = DirectoryManager()
# print(dm.get_files_in_folder("./from"))