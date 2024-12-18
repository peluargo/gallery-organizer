from factories.folder_factory import FolderFactory
from models.organizer import Organizer


class OrganizerFactory:
    def __init__(self, folder_factory: FolderFactory):
        self._folder_factory = folder_factory

    def create(
        self,
        origin_path: str,
        destination_path: str,
        must_preserve_original_files: bool = False,
        must_rename_files: bool = False,
    ):
        origin = self._folder_factory.create_from_path(origin_path)
        destination = self._folder_factory.create_from_path(destination_path)

        return Organizer(
            origin,
            destination,
            must_preserve_original_files,
            must_rename_files,
            self._folder_factory,
        )
