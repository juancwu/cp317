from abc import ABC, abstractmethod

"""
Abstract class for file processor
It has two methods: open_file and close_file
open_file: given a file path, it opens the file and returns the file object
close_file: given a file object, it closes the file
"""
class FileProcessor(ABC):
    @abstractmethod
    def open_file(self, file_path):
        pass

    @abstractmethod
    def close_file(self, file_object):
        pass