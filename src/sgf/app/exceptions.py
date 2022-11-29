from colorama import Fore

# ==================== WARNINGS ====================
class MissMatchWarning(Exception):
    def __init__(self, student_id: str, missing_in: str):
        self.student_id = student_id
        self.missing_in = missing_in

        # construct the message
        self.message = Fore.YELLOW + "WARNING: " + Fore.RESET
        self.message += "Missing " + Fore.BLUE + self.student_id + Fore.RESET
        self.message += " in " + Fore.BLUE + self.missing_in + Fore.RESET

    def __str__(self) -> str:
        return self.message

class OverrideWarning(Exception):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        self.message = Fore.YELLOW + "WARNING: " + Fore.RESET
        self.message += f"Overriding {Fore.BLUE + self.file_path + Fore.RESET}. IRREVERSIBLE ACTION!"

    def __str__(self) -> str:
        return self.message
# ==================== WARNINGS ====================

# ==================== ERRORS ====================
class FileDoesNotExistsError(Exception):
    def __init__(self, file_path: str):
        self.message = Fore.RED + "ERROR: " + Fore.RESET + f"‘{Fore.BLUE + file_path + Fore.RESET}’ does not exist or is not a file"

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

class ReadPermissionError(Exception):
    def __init__(self, file_path: str):
        self.message = Fore.RED + "ERROR: " + Fore.RESET + f"Permission denied to read {Fore.BLUE + file_path + Fore.RESET}"

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

class WritePermissionError(Exception):
    def __init__(self, file_path: str):
        self.message = Fore.RED + "ERROR: " + Fore.RESET + f"Permission denied to write/create a file in {Fore.BLUE + file_path + Fore.RESET}"

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

class NoOpenFileError(Exception):
    def __init__(self):
        self.message = Fore.RED + "ERROR: " + Fore.RESET + "No open file to do I/O operations"

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

class MissingValueError(Exception):
    def __init__(self, line_number: int, input_file: str) -> None:
        self.message = Fore.RED + "ERROR: " + Fore.RESET + f"Missing value in {Fore.BLUE + input_file + Fore.RESET} at line {Fore.BLUE}{line_number}{Fore.RESET}"

        super().__init__(self.message)
    
    def __str__(self) -> str:
        return self.message

class IncorrectDataTypeError(Exception):
    def __init__(self, line_number: int, input_file: str) -> None:
        self.message = Fore.RED + "ERROR: " + Fore.RESET + f"Incorrect data type in {Fore.BLUE + input_file + Fore.RESET} at line {Fore.BLUE}{line_number}{Fore.RESET}"

        super().__init__(self.message)
    
    def __str__(self) -> str:
        return self.message

class QuitException(Exception):
    def __init__(self):
        self.message = Fore.RED + "Received '!q'. The program will try to quit gracefully..." + Fore.RESET

        super().__init__(self.message)
    
    def __str__(self) -> str:
        return self.message
# ==================== ERRORS ====================