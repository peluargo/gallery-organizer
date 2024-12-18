from models.folder import Folder
from .image_factory import ImageFactory
import os
import filetype


class FolderFactory:
    def __init__(self, image_factory: ImageFactory):
        self._image_factory = image_factory

    def create_from_path(self, path: str) -> Folder:
        return Folder(
            name=os.path.basename(path),
            path=os.path.abspath(path),
            images=[
                self._image_factory.create_from_path(
                    os.path.join(os.path.abspath(path), file_path)
                )
                # the 'os.walk' returns a tuple containing the path, folders and files
                # we use 'sum' to flatten the list of files
                for file_path in sum([values[2] for values in os.walk(path)], [])
                # we only create an Image instance for the image files
                if filetype.is_image(os.path.join(path, file_path))
            ],
            folders=[
                # we recursively create Folder instances
                self.create_from_path(folder_path)
                # the 'os.walk' returns a tuple containing the path, folders and files
                # we use 'sum' to flatten the list of folders
                for folder_path in sum([values[1] for values in os.walk(path)], [])
            ],
        )
