from .file_handler import FileHandler
from .exceptions import NoOpenFileError

class Writer(FileHandler):
    def __init__(self):
        super().__init__()

    def write(self, data: str):
        # check if there is an opened file
        if self.is_closed():
            raise NoOpenFileError()

        self._file.write(data)

        return