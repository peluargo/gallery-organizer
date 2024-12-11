import os
import shutil
from datetime import datetime
from PIL import Image
from ProgressBar import *

class Organizer():
    def __init__(self, origin, destination, preserve_origin_files = True, progress_bar = ProgressBar()):
        self.origin = origin
        self.destination = destination
        self.move_method = self.move_file_preserving_origin if preserve_origin_files else self.move_file_removing_origin
        self.progress_bar = progress_bar

    def get_origin_files(self):
        return [f for f in os.listdir(self.origin) if os.path.isfile(os.path.join(self.origin, f))]
    
    def get_destination_folders(self):
        return [f for f in os.listdir(self.destination) if os.path.isdir(os.path.join(self.destination, f))]
    
    def get_creation_date_from_file(self, filePath):
        return Image.open(filePath).getexif().get(306)
    
    def get_file_extension(self, filePath):
        return os.path.splitext(filePath)[1]

    def convert_creation_date_format(self, creation_date):
        return datetime.strftime(datetime.strptime(creation_date, '%Y:%m:%d %H:%M:%S'), '%Y-%m')

    def get_destination_folder_name(self, filePath):
        creation_date = self.get_creation_date_from_file(filePath)
        return self.convert_creation_date_format(creation_date) if creation_date is not None else 'Unknown Date'
    
    def destination_folder_exists(self, destinationFolderName):
        return destinationFolderName in self.get_destination_folders()
    
    def create_destination_folder(self, destinationFolderName):
        destinationFolderPath = self.destination + "/" + destinationFolderName
        os.mkdir(destinationFolderPath)
        return destinationFolderPath
    
    def move_file_preserving_origin(self, fileSourcePath, fileDestinationPath):
        shutil.copy(fileSourcePath, fileDestinationPath)
    
    def move_file_removing_origin(self, fileSourcePath, fileDestinationPath):
        shutil.move(fileSourcePath, fileDestinationPath)

    def move_file(self, file):
        file_source_path = self.origin + "/" + file

        destinationFolderName = self.get_destination_folder_name(file_source_path)

        if not self.destination_folder_exists(destinationFolderName):
            self.create_destination_folder(destinationFolderName)

        file_destination_path = self.destination + "/" + destinationFolderName + "/" + file

        self.move_method(file_source_path, file_destination_path)

    def move_files(self):
        print(r"""
              ____       _ _                            
             / ___| __ _| | | ___ _ __ _   _            
            | |  _ / _` | | |/ _ \ '__| | | |           
            | |_| | (_| | | |  __/ |  | |_| |           
             \____|\__,_|_|_|\___|_|   \__, |           
              ___                      |___/            
             / _ \ _ __ __ _  __ _ _ __ (_)_______ _ __ 
            | | | | '__/ _` |/ _` | '_ \| |_  / _ \ '__|
            | |_| | | | (_| | (_| | | | | |/ /  __/ |   
             \___/|_|  \__, |\__,_|_| |_|_/___\___|_|   
                       |___/                            
        """)
        print('\n\n')

        for file in self.get_origin_files():
            self.move_file(file)
            self.progress_bar.increment()
            self.progress_bar.display()
            
        print('Done!')

    def config_progress_bar(self):
        self.progress_bar.total = len(self.get_origin_files())

    def run(self):
        self.config_progress_bar()
        self.move_files()