from abstracts.writer_abstract import WriterAbstract
from io import TextIOWrapper
import os
from copy import deepcopy

class Writer(WriterAbstract):
    def __init__(self):
        self._is_closed = True
        self._file = None

    @property
    def is_closed(self):
        return deepcopy(self._is_closed)

    def write(self, data: str):
        #Needs to write down the formatter first
        assert self._file, 'Open file first'
        assert isinstance(self._file, TextIOWrapper), 'File object must be a TextIOWrapper'
        assert not self._file.closed, 'File is closed'

        bytes_written = self._file.write(data)
        self._bytes_written += bytes_written

        return bytes_written

    def open_file(self, file_path: str) -> bool:
        
        if not isinstance(file_path, str):
            return False, 'File path must be a string'
        
        if os.path.exists(file_path):
            print("File already exists, do you want to override? [y/n]", end=" ")
            override = input()
            if override != 'y':
                return False, 'File already exists'

        try:
            file_object = open(file_path, 'w')
        except Exception as e:
            return False, str(e)
        
        self._file = file_object

        return True


    def close_file(self) -> int:
        if not self._file:
            return False

        self._file.close()

        self._file = None

        return True