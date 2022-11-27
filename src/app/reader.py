from abstracts.reader_abstract import FileHandlerAbstract
from abstracts.reader_abstract import ReaderAbstract
from io import TextIOWrapper
import os

class FileHandler(FileHandlerAbstract):
    def __init__(self):
        self._file = None
        self._is_closed = True

    def open_file(self, file_path: str, mode: str) -> bool:
        self._file = open(file_path, mode)
        return True

class Reader(FileHandler):
    def __init__(self) -> None:
        super().__init__()
        self._file = None
        self._is_closed = True

    def read(self, bytes_to_read: int = 16):

        data = self.file.read(bytes_to_read)
        self._bytes_read += bytes_to_read

        return data


    def close_file(self) -> bool:
        assert self._file, 'No file object provided'
        assert isinstance(self.file, TextIOWrapper), 'File object must be a TextIOWrapper'

        self._file.close()

        return True