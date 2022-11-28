import unittest
from src.app.exceptions import MissingValueError, MissMatchWarning, OverrideWarning, FileDoesNotExistsError, ReadPermissionError, WritePermissionError, NoOpenFileError, IncorrectDataTypeError
from tests.colours import *

class ExceptionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file = "test.txt"
        self.test_line = "1"
        self.test_student_id = "123456789"
    
    def test_missing_value_error(self):

        with self.assertRaises(MissingValueError) as cm:
            raise MissingValueError(self.test_line, self.test_file)
        
        message = f'{RED}ERROR: {RESET}Missing value in {BLUE + self.test_file + RESET} at line {BLUE + self.test_line + RESET}'
        self.assertEqual(str(cm.exception), message)

    def test_miss_match_warning(self):
            with self.assertRaises(MissMatchWarning) as cm:
                raise MissMatchWarning(self.test_student_id, self.test_file)
            
            message = f'{YELLOW}WARNING: {RESET}Missing {BLUE + self.test_student_id + RESET} in {BLUE + self.test_file + RESET}'
            self.assertEqual(str(cm.exception), message)
    
    def test_override_warning(self):
        with self.assertRaises(OverrideWarning) as cm:
            raise OverrideWarning(self.test_file)
        
        message = f'{YELLOW}WARNING: {RESET}Overriding {BLUE + self.test_file + RESET}. IRREVERSIBLE ACTION!'
        self.assertEqual(str(cm.exception), message)

    def test_file_does_not_exists_error(self):
        with self.assertRaises(FileDoesNotExistsError) as cm:
            raise FileDoesNotExistsError(self.test_file)
        
        message = f'{RED}ERROR: {RESET}‘{BLUE + self.test_file + RESET}’ does not exist or is not a file'
        self.assertEqual(str(cm.exception), message)
    
    def test_read_permission_error(self):
        with self.assertRaises(ReadPermissionError) as cm:
            raise ReadPermissionError(self.test_file)
        
        message = f'{RED}ERROR: {RESET}Permission denied to read {BLUE + self.test_file + RESET}'
        self.assertEqual(str(cm.exception), message)
    
    def test_write_permission_error(self):
        with self.assertRaises(WritePermissionError) as cm:
            raise WritePermissionError(self.test_file)
        
        message = f'{RED}ERROR: {RESET}Permission denied to write/create a file in {BLUE + self.test_file + RESET}'
        self.assertEqual(str(cm.exception), message)
    
    def test_no_open_file_error(self):
        with self.assertRaises(NoOpenFileError) as cm:
            raise NoOpenFileError()
        
        message = f'{RED}ERROR: {RESET}No open file to do I/O operations'
        self.assertEqual(str(cm.exception), message)

    def test_incorrect_data_type_error(self):
        with self.assertRaises(IncorrectDataTypeError) as cm:
            raise IncorrectDataTypeError(self.test_line, self.test_file)
        
        message = f'{RED}ERROR: {RESET}Incorrect data type in {BLUE + self.test_file + RESET} at line {BLUE + self.test_line + RESET}'
        self.assertEqual(str(cm.exception), message)
    
        