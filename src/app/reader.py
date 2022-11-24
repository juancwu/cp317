from abstracts.reader_abstract import ReaderAbstract
from io import TextIOWrapper
import os

class Reader(ReaderAbstract):
    def __init__(self) -> None:
        super().__init__()
        self._bytes_read = 0
        self._file = None

    def read(self, bytes_to_read: int = 16):
        assert self.file, 'Open file first'
        assert isinstance(self.file, TextIOWrapper), 'File object must be a TextIOWrapper'

        data = self.file.read(bytes_to_read)
        self._bytes_read += bytes_to_read

        return data

    def open_file(self, file_path: str) -> bool:

        assert file_path, 'No file path provided'
        assert isinstance(file_path, str), 'File path must be a string'
        assert os.path.exists(file_path), 'File does not exist'
        assert os.path.isfile(file_path), 'File path must be a file'
        
        try:
            file_object = open(file_path, 'r')
        except Exception as e:
            print("ERROR (FileProcessor): ", str(e))
            return False
        
        self._file = file_object

        return True


    def close_file(self) -> None:
        assert self.file, 'No file object provided'
        assert isinstance(self.file, TextIOWrapper), 'File object must be a TextIOWrapper'

        self.file.close()

        return