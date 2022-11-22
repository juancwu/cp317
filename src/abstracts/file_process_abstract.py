from abc import ABC, abstractmethod
from io import TextIOWrapper
"""
Abstract class for file processor
It has two methods: open_file and close_file
open_file: given a file path, it opens the file and returns the file object
close_file: given a file object, it closes the file
"""
class FileProcessorAbstract(ABC):
    @abstractmethod
    def open_file(self, file_path: str) -> TextIOWrapper or None:
        pass

    @abstractmethod
    def close_file(self, file_object: TextIOWrapper) -> None:
        pass