import os
import shutil
from typing import List
import uuid
from factories.folder_factory import FolderFactory
from models.folder import Folder
from datetime import datetime

from models.image import Image


class Organizer:
    def __init__(
        self,
        origin: Folder,
        destination: Folder,
        must_preserve_original_images: bool = False,
        must_rename_images: bool = False,
        folder_factory: FolderFactory = None,
    ):
        self._origin = origin
        self._destination = destination
        self._must_preserve_original_images = must_preserve_original_images
        self._must_rename_images = must_rename_images
        self._folder_factory = folder_factory

    def _determine_folder_name(self, file_creation_date):
        if file_creation_date is None:
            return "unknown-date"

        return datetime.strftime(file_creation_date, "%Y-%m")

    def _get_folder(self, folder_name: str) -> Folder:
        if self._destination.has_folder(folder_name):
            return self._destination.get_folder(folder_name)

        # we create the folder if it does not exist
        folder_path = os.path.normpath(
            os.path.join(self._destination.get_path() + "/" + folder_name)
        )
        folder = self._folder_factory.create_from_path(folder_path)

        self._destination.add_folder(folder)

        return folder

    def _organize_destination_in_folders(self, images: List[Image]):
        for image in images:
            folder_name = self._determine_folder_name(image.get_creation_date())

            folder = self._get_folder(folder_name)

            # we rename the image if the user wants to
            # for this we set the image name to a random uuid
            if self._must_rename_images:
                image.set_name(str(uuid.uuid4()))

            # we update the image path to the new folder path
            image.set_path(
                os.path.normpath(
                    os.path.join(
                        folder.get_path() + "/" + image.get_name_with_extension()
                    )
                )
            )
            folder.add_file(image)

        return self._destination.get_folders()

    def _move_images(self, images: List[Image]):
        for image in images:
            if self._must_preserve_original_images:
                shutil.copy(image.get_original_path(), image.get_path())
            else:
                shutil.move(image.get_original_path(), image.get_path())

    def _create_folders(self, folders: List[Folder]):
        for folder in folders:
            # we first create the destination folder
            os.makedirs(folder.get_path(), exist_ok=True)

            # then we move the folder images
            self._move_images(folder.get_images())

    def run(self):
        images = self._origin.get_images()

        folders = self._organize_destination_in_folders(images)

        for folder in folders:
            print(folder.get_name())
            for image in folder.get_images():
                print("- " + image.get_original_name() + " -> " + image.get_name())

        self._create_folders(folders)
