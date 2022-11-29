from ..abstracts.file_handler_abstract import FileHandlerAbstract
from .exceptions import FileDoesNotExistsError, ReadPermissionError, WritePermissionError, QuitException
import os
from colorama import Fore

class FileHandler(FileHandlerAbstract):
    def __init__(self) -> None:
        self._file = None
        self._is_closed = True
        self._file_path = ""
    
    def open_file(self, file_path: str, mode: str) -> str:
        # if file is already open, do nothing
        if not self._is_closed:
            return file_path

        # check for valid mode
        if mode not in ["r", "w"]:
            raise Exception("Invalid mode. Mode must be 'r' or 'w'")
        
        # if read mode check if file exists and if it is a file
        if mode == "r":
            if not os.path.isfile(file_path):
                raise FileDoesNotExistsError(file_path)
            if not os.access(file_path, os.R_OK):
                raise ReadPermissionError(file_path)
        elif mode == "w":
            if os.path.isdir(file_path):
                raise FileDoesNotExistsError(file_path)
            
            # if write mode check if file exists and if it is a file
            # ask for override permission
            while os.path.exists(file_path) or file_path == "":
                if os.path.isdir(file_path):
                    print("Invalid file path. Path is a directory")
                    file_path = input("Enter a valid file path (!q to quit): ")
                    if file_path == "!q":
                        raise QuitException()
                else:
                    override_permission = input(f"File {Fore.BLUE + file_path + Fore.RESET} already exists. Do you want to override it? (y/n or !q to quit): ")
                    if override_permission == "!q":
                        raise QuitException()
                    elif override_permission != "y":
                        # rename output filename
                        file_path = input(f"Enter new file name (enter !q to quit): ")
                        if file_path == "!q":
                            raise QuitException()
                    else:
                        if not os.access(file_path, os.W_OK):
                            raise WritePermissionError(file_path)
                        break
        # create file
        self._file = open(file_path, mode)
        self._is_closed = False

        self._file_path = file_path

        return file_path
    
    def close_file(self) -> None:
        # if file is already closed, do nothing
        if self._is_closed:
            return
        
        # close file
        self._file.close()
        self._is_closed = True
        self._file = None

        return

    def is_closed(self):
        return self._is_closed

    def get_file_path(self):
        return self._file_path
