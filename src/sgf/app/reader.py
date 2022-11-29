from .file_handler import FileHandler
from .exceptions import NoOpenFileError

class Reader(FileHandler):
    def __init__(self) -> None:
        super().__init__()

    def read(self):

        # check for open file
        if self.is_closed():
            raise NoOpenFileError()

        # read from file
        line = self._file.readline()
        return line