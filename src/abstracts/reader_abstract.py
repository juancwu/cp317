from abc import ABC, abstractmethod

"""
Abstract class for reader class
It has three methods: open_file and close_file and read
open_file: given a file path, it opens the file and returns the file object, override from file_process class
close_file: given a file object, it closes the file, override from file_process class
read: given a file, we can read the file and use formatter to format the string inside the file given
"""
class ReaderAbstract(ABC):
    @abstractmethod
    def read(self, bytes_to_read: int) -> str:
        pass

    @abstractmethod
    def open_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def close_file(self) -> None:
        pass
    