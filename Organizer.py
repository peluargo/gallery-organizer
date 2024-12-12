import os
import shutil
import uuid
from datetime import datetime
from PIL import Image
from Mapper import Mapper
from Logger import Logger

class Organizer():
    def __init__(self, origin, 
                 destination, 
                 preserve_original_files = True, 
                 rename_files = False,
                 mapper = Mapper(), 
                 logger = Logger()):
        self._origin = origin
        self._destination = destination
        self._rename_files = rename_files
        self._move_method = self._move_file_preserving_origin if preserve_original_files else self._move_file_removing_origin
        self._action = 'Copying' if preserve_original_files else 'Moving'
        self._mapper = mapper
        self._logger = logger

    def _get_origin_files(self):
        return [f for f in os.listdir(self._origin) if os.path.isfile(os.path.join(self._origin, f))]
    
    def _get_destination_folders(self):
        return [f for f in os.listdir(self._destination) if os.path.isdir(os.path.join(self._destination, f))]
    
    def _get_creation_date_from_file(self, filePath):
        return Image.open(filePath).getexif().get(306)
    
    def _get_file_extension(self, filePath):
        return os.path.splitext(filePath)[1]

    def _convert_creation_date_format(self, creation_date):
        return datetime.strftime(datetime.strptime(creation_date, '%Y:%m:%d %H:%M:%S'), '%Y-%m')

    def _get_destination_folder_name(self, filePath):
        creation_date = self._get_creation_date_from_file(filePath)
        return self._convert_creation_date_format(creation_date) if creation_date is not None else 'unknown-date'
    
    def _destination_folder_exists(self, destinationFolderName):
        return destinationFolderName in self._get_destination_folders()
    
    # TODO: verify if file with the same name already exists in folder
    def _get_new_unique_file_name(self, file):
        return str(uuid.uuid4()) + self._get_file_extension(file)
    
    def _get_destination_path(self, file, destination_folder_name):
        file_name = self._get_new_unique_file_name(file) if self._rename_files else file
        return self._destination + "/" + destination_folder_name + "/" + file_name
    
    def _file_exists(self, filePath):
        return os.path.isfile(filePath)
    
    def _create_destination_folder(self, destinationFolderName):
        destinationFolderPath = self._destination + "/" + destinationFolderName
        os.mkdir(destinationFolderPath)
        return destinationFolderPath
    
    def _move_file_preserving_origin(self, fileSourcePath, fileDestinationPath):
        shutil.copy(fileSourcePath, fileDestinationPath)
    
    def _move_file_removing_origin(self, fileSourcePath, fileDestinationPath):
        shutil.move(fileSourcePath, fileDestinationPath)

    def _move_file(self, file):
        file_source_path = self._origin + "/" + file

        destination_folder_name = self._get_destination_folder_name(file_source_path)

        if not self._destination_folder_exists(destination_folder_name):
            self._create_destination_folder(destination_folder_name)

        file_destination_path = self._get_destination_path(file, destination_folder_name)

        self._move_method(file_source_path, file_destination_path)

        self._mapper.map(file, file_source_path, file_destination_path)
        self._log_moving_file(file_source_path, file_destination_path)

    def _move_files(self):
        self._logger.log(f'{self._action} {len(self._get_origin_files())} files:')
        for file in self._get_origin_files():
            self._move_file(file)

    def _log_title(self):
        self._logger.log(r"""
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
        self._logger.log('\n')

    def _log_resolution(self):
        self._logger.log('Done!')

    def _log_moving_file(self, fromPath, toPath):
        self._logger.log(f' - {self._action} "{fromPath}" to "{toPath}"')

    def run(self):
        self._log_title()
        self._move_files()
        self._log_resolution()