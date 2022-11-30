from src.app.file_handler import FileHandler
from src.app.exceptions import FileDoesNotExistsError, ReadPermissionError, WritePermissionError
from tests.colours import *
import io
import unittest
from unittest.mock import patch
import os

class FileHandlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.file_handler = FileHandler()
        self.test_file_path = "tests/data/test_file.txt"
        self.invalid_test_file_path = "tests/data/non_existing_file.txt"
        self.no_read_file_path = "tests/data/no_read.txt"
        self.no_write_file_path = "tests/data/no_write.txt"
        self.tmp_test_file_path = "tests/data/tmp.txt"

        # initial test clean up
        if os.path.exists(self.no_read_file_path):
            os.remove(self.no_read_file_path)
        if os.path.exists(self.no_write_file_path):
            os.remove(self.no_write_file_path)
        if os.path.exists(self.tmp_test_file_path):
            os.remove(self.tmp_test_file_path)

        if not os.path.exists("tests/data"):
            os.mkdir("tests/data")
        
        # create test file
        with open(self.test_file_path, "w") as file:
            file.write("test")
        
    
        super().setUp()
    
    def test_open_file_read_mode(self):
        self.assertTrue(self.file_handler.is_closed())
        self.file_handler.open_file(self.test_file_path, "r")
        self.assertFalse(self.file_handler.is_closed())
        self.assertIsInstance(self.file_handler._file, io.TextIOWrapper)
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)

    def test_open_file_write_mode(self):
        # testing create a file for output
        self.assertTrue(self.file_handler.is_closed())
        self.file_handler.open_file(self.tmp_test_file_path, "w")
        self.assertFalse(self.file_handler.is_closed())
        self.assertIsInstance(self.file_handler._file, io.TextIOWrapper)
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)

        # clean up
        os.remove(self.tmp_test_file_path)
    # patch stdin to simulate user input
    @patch("builtins.input", return_value="y")
    def test_open_file_override(self, input_mock):        
        # create test file with content "testing override"
        with open(self.tmp_test_file_path, "w") as file:
            file.write("testing override")
        
        # open file in write mode
        self.file_handler.open_file(self.tmp_test_file_path, "w")
        self.assertFalse(self.file_handler.is_closed())
        
        # override
        self.file_handler._file.write("override successful")
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())

        # check if file is override
        with open(self.tmp_test_file_path, "r") as file:
            self.assertEqual(file.read(), "override successful")
        
        # clean up
        os.remove(self.tmp_test_file_path)

    # patch stdin to simulate user input
    @patch("builtins.input")
    def test_open_file_no_override(self, input_mock):
        new_file_path = "tests/data/tmp2.txt"
        new_file_content = "no override"
        old_file_content = "testing override"
        
        # sequence of user input
        input_mock.side_effect = ["n", new_file_path]

        # create test file with content "testing override"
        with open(self.tmp_test_file_path, "w") as file:
            file.write(old_file_content)
        
        # open file in write mode
        self.file_handler.open_file(self.tmp_test_file_path, "w")
        self.assertFalse(self.file_handler.is_closed())

        # write new content
        self.file_handler._file.write(new_file_content)
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())

        # check for new content in file
        with open(new_file_path, "r") as file:
            self.assertEqual(file.read(), new_file_content)
        
        # check for old file content
        with open(self.tmp_test_file_path, "r") as file:
            self.assertEqual(file.read(), old_file_content)
        
        # clean up
        os.remove(self.tmp_test_file_path)
        os.remove(new_file_path)
    
    def test_open_file_read_directory(self):
        self.assertTrue(self.file_handler.is_closed())
        with self.assertRaises(Exception):
            self.file_handler.open_file("tests/data", "r")
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)
    
    @patch("builtins.input", return_value="y")
    def test_open_file_override_no_write_permission(self, _):
        # create test file with content "testing override" and no write permission
        with open(self.no_write_file_path, "w") as file:
            file.write("testing override")
        os.chmod(self.no_write_file_path, 0o444)

        # open file in write mode
        self.assertTrue(self.file_handler.is_closed())
        # expect no write permission error
        with self.assertRaises(WritePermissionError):
            self.file_handler.open_file(self.no_write_file_path, "w")
        self.assertTrue(self.file_handler.is_closed())

        # clean up
        os.remove(self.no_write_file_path)
        
    def test_open_file_invalid_mode(self):
        self.assertTrue(self.file_handler.is_closed())
        with self.assertRaises(Exception):
            self.file_handler.open_file(self.test_file_path, "x")
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)

    def test_open_file_invalid_file_path(self):
        self.assertTrue(self.file_handler.is_closed())
        with self.assertRaises(FileDoesNotExistsError):
            self.file_handler.open_file(self.invalid_test_file_path, "r")
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)
    
    def test_close_file(self):
        self.assertTrue(self.file_handler.is_closed())
        self.file_handler.open_file(self.test_file_path, "r")
        self.assertFalse(self.file_handler.is_closed())
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)

    def test_close_file_already_closed(self):
        self.assertTrue(self.file_handler.is_closed())
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)
    
    def test_is_closed(self):
        self.assertTrue(self.file_handler.is_closed())
        self.file_handler.open_file(self.test_file_path, "r")
        self.assertFalse(self.file_handler.is_closed())
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())

    def test_no_read_permission(self):
        self.assertTrue(self.file_handler.is_closed())

        # create test file with no read permission
        with open(self.no_read_file_path, "w") as file:
            file.write("test")
        os.chmod(self.no_read_file_path, 0o200)

        with self.assertRaises(ReadPermissionError):
            self.file_handler.open_file(self.no_read_file_path, "r")
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)

        # clean up
        os.remove(self.no_read_file_path)

    def test_try_reopen_opened_file(self):
        self.assertTrue(self.file_handler.is_closed())
        self.file_handler.open_file(self.test_file_path, "r")
        self.assertFalse(self.file_handler.is_closed())

        # try reopen
        self.file_handler.open_file(self.test_file_path, "r")
        
        self.assertFalse(self.file_handler.is_closed())
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())

    def test_open_file_write_directory(self):
        self.assertTrue(self.file_handler.is_closed())
        with self.assertRaises(Exception):
            self.file_handler.open_file("tests/data", "w")
        self.assertTrue(self.file_handler.is_closed())
        self.assertIsNone(self.file_handler._file)

    @patch("builtins.input")
    def test_open_file_write_no_override_directory(self, input_mock):
        new_file_path = "tests/data/tmp2.txt"

        # populate input sequence
        input_mock.side_effect = ["n", "tests/data", new_file_path]
        
        # create a test file
        with open(self.tmp_test_file_path, "w") as file:
            file.write("test")
        
        # open file in write mode
        self.assertTrue(self.file_handler.is_closed())
        self.file_handler.open_file(self.tmp_test_file_path, "w")
        self.assertFalse(self.file_handler.is_closed())

        # close file
        self.file_handler.close_file()
        self.assertTrue(self.file_handler.is_closed())

        # check for new file existence
        self.assertTrue(os.path.exists(new_file_path))
        
        # check for old content
        with open(self.tmp_test_file_path, "r") as file:
            self.assertEqual(file.read(), "test")
        
        # clean up
        os.remove(self.tmp_test_file_path)
        os.remove(new_file_path)
    
    def tearDown(self) -> None:
        # after tests cleanup
        if os.path.exists(self.no_read_file_path):
            os.remove(self.no_read_file_path)
        if os.path.exists(self.no_write_file_path):
            os.remove(self.no_write_file_path)
        if os.path.exists(self.tmp_test_file_path):
            os.remove(self.tmp_test_file_path)

        self.file_handler = None
        self.test_file_path = None
        self.invalid_test_file_path = None
        self.no_read_file_path = None
        self.no_write_file_path = None

        super().tearDown()