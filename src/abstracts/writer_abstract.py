from abc import ABC, abstractmethod

"""
Abstract class for writer class
It has three methods: open_file and close_file and read
open_file: given a file path, it opens the file and returns the file object, override from file_process class
close_file: given a file object, it closes the file, override from file_process class
write: given a file, we can write the file and use write in formatted string
"""
class WriterAbstract(ABC):
    @property
    def is_closed(self):
        pass

    @abstractmethod
    def write(self, data: str) -> int:
        pass

    @abstractmethod
    def open_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def close_file(self) -> bool:
        pass
