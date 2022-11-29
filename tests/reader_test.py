from src.sgf.app.reader import Reader
from src.sgf.app.exceptions import NoOpenFileError
import unittest
import os
import io

class ReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.reader = Reader()
        self.test_file_path = "tests/data/test_file.txt"
        self.invalid_test_file_path = "tests/data/non_existing_file.txt"
        self.test_file_content = "test"
        
        if not os.path.exists("tests/data"):
            os.mkdir("tests/data")
        
        # create test file
        with open(self.test_file_path, "w") as file:
            file.write(self.test_file_content)
        
        super().setUp()
    
    def test_read(self):
        # open file
        self.reader.open_file(self.test_file_path, "r")
        self.assertFalse(self.reader.is_closed())
        self.assertIsInstance(self.reader._file, io.TextIOWrapper)
        
        # read from file
        line = self.reader.read()
        self.assertEqual(line, self.test_file_content)
        
        # close file
        self.reader.close_file()
        self.assertTrue(self.reader.is_closed())
        self.assertIsNone(self.reader._file)
    
    def test_read_no_open_file(self):
        with self.assertRaises(NoOpenFileError):
            self.reader.read()