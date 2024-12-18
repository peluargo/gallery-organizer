from datetime import datetime
from PIL import Image as PilImage
from models.image import Image
import os


class ImageFactory:
    def create_from_path(self, path: str):
        name = os.path.splitext(os.path.basename(path))[0]
        path = os.path.abspath(path)
        extension = os.path.splitext(os.path.basename(path))[1]
        creation_date_string = PilImage.open(path).getexif().get(306)
        creation_date = (
            datetime.strptime(creation_date_string, "%Y:%m:%d %H:%M:%S")
            if creation_date_string is not None
            else None
        )

        return Image(name, path, extension, creation_date)
