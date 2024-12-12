from MapFile import MapFile
from Status import Status

class Mapper:
    def __init__(self, map_file = MapFile()):
        self.map_file = map_file

    def map(self, name, from_path, to_path):
        self.map_file.insert({'name': name, 'from_path': from_path, 'to_path': to_path})

    def start(self):
        self.map_file.set_status(Status.STARTED)

    def abort(self, message):
        self.map_file.set_status(Status.ABORTED)
        self.map_file.set_message(message)

    def finish(self):
        self.map_file.set_status(Status.FINISHED)