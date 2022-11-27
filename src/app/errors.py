from abstracts.errors_abstract import *
from colorama import Fore

class MissMatchError(MissMatchErrorAbstract):
    def __init__(self, student_id: str, missing_in: str):
        self.student_id = student_id
        self.missing_in = missing_in

    def __str__(self) -> str:
        error_msg = Fore.RED + "ERROR: " + Fore.RESET
        error_msg += "Missing " + Fore.YELLOW + self.student_id + Fore.RESET
        error_msg += " in " + Fore.YELLOW + self.missing_in + Fore.RESET
        return error_msg

class ReadFromClosedFilError(ReadFromClosedFileErrorAbstract):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def __str__(self) -> str:
        error_msg = Fore.RED + "ERROR: " + Fore.RESET
        error_msg += "Cannot read from closed file " + Fore.YELLOW + self.file_path + Fore.RESET
        error_msg += ". Re-open file with open_file() method."
        return error_msg

class WriteToClosedFileError(WriteToClosedFileErrorAbstract):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def __str__(self) -> str:
        error_msg = Fore.RED + "ERROR: " + Fore.RESET
        error_msg += "Cannot write to closed file " + Fore.YELLOW + self.file_path + Fore
        error_msg += ". Re-open file with open_file() method."
        return error_msg
    