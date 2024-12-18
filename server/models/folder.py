from .image import Image
from typing import List, Self


class Folder:
    def __init__(
        self, name: str, path: str, images: List[Image] = [], folders: List[Self] = []
    ):
        self._name = name
        self._path = path
        self._images = images
        self._folders = folders

    # getters and setters

    def get_name(self) -> str:
        return self._name

    def get_path(self) -> str:
        return self._path

    def get_images(self) -> List[Image]:
        return self._images

    def get_folders(self) -> List[Self]:
        return self._folders

    def set_name(self, name) -> None:
        self._name = name

    def set_path(self, path) -> None:
        self._path = path

    def set_images(self, images) -> None:
        self._images = images

    def set_folders(self, folders) -> None:
        self._folders = folders

    # methods for managing images

    def add_file(self, file: Image) -> None:
        self._images.append(file)

        # we sort the remaining images for good measure
        self.sort_images()

    def sort_images(self) -> None:
        self._images.sort(key=lambda image: image.get_name())

    def get_image(self, image_name: str) -> Image:
        return [i for i in self.get_images() if i.get_name() == image_name][0]

    def remove_file(self, image_name: str) -> Image:
        images = self.get_images()

        # filters out the file by its name
        removed_image = list(filter(lambda x: image_name == x.get_name(), images))

        # gets a new list without the removed file
        updated_image_list = list(set(images) - set(removed_image))

        self.set_images(updated_image_list)

        # we sort the remaining images for good measure
        self.sort_images()

        return removed_image

    # methods for managing subfolders

    def add_folder(self, folder: Self) -> None:
        self._folders.append(folder)

        # we sort the remaining folders for good measure
        self.sort_folders()

    def sort_folders(self) -> None:
        self._folders.sort(key=lambda folder: folder.get_name())

    def has_folder(self, folder_name: str) -> bool:
        return folder_name in [folder.get_name() for folder in self.get_folders()]

    def get_folder(self, folder_name: str) -> Self:
        return [
            folder for folder in self.get_folders() if folder.get_name() == folder_name
        ][0]
