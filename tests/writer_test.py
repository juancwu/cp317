from src.app.writer import Writer
from src.app.exceptions import NoOpenFileError
from unittest.mock import patch
import unittest
import os
import io

class WriterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file_path = "tests/data/test_file.txt"
        self.test_file_path_override = "tests/data/test_file_override.txt"
        self.test_file_content = "test"
        self.test_file_override_content = "test_override"
        self.writer = Writer()
        
        # create test environemtn
        if not os.path.exists("tests/data"):
            os.mkdir("tests/data")

        # before test clean up
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.test_file_path_override):
            os.remove(self.test_file_path_override)
        
        
        super().setUp()
    
    def test_write_new(self):
        # open file
        self.writer.open_file(self.test_file_path, "w")
        self.assertFalse(self.writer.is_closed())
        self.assertIsInstance(self.writer._file, io.TextIOWrapper)
        
        # write to file
        self.writer.write(self.test_file_content)
        
        # close file
        self.writer.close_file()
        self.assertTrue(self.writer.is_closed())
        self.assertIsNone(self.writer._file)

        # check if file was created
        self.assertTrue(os.path.exists(self.test_file_path))
        with open(self.test_file_path, "r") as file:
            self.assertEqual(file.read(), self.test_file_content)
        
    @patch("builtins.input", return_value="y")
    def test_write_override(self, _):
        # open file
        self.assertTrue(self.writer.is_closed())
        self.writer.open_file(self.test_file_path, "w")
        self.assertFalse(self.writer.is_closed())

        # write to file
        self.writer.write(self.test_file_override_content)

        # close file
        self.writer.close_file()
        self.assertTrue(self.writer.is_closed())

        # check if file was created
        self.assertTrue(os.path.exists(self.test_file_path))
        with open(self.test_file_path, "r") as file:
            self.assertEqual(file.read(), self.test_file_override_content)
        
    @patch("builtins.input")
    def test_write_no_override(self, input_mock):
        # populate user input sequence
        input_mock.side_effect = ["n", self.test_file_path_override]

        # create test file
        with open(self.test_file_path, "w") as file:
            file.write(self.test_file_content)
    
        # open file
        self.assertTrue(self.writer.is_closed())
        self.writer.open_file(self.test_file_path, "w")
        self.assertFalse(self.writer.is_closed())

        # write to file
        self.writer.write(self.test_file_override_content)

        # close file
        self.writer.close_file()

        # check if file was created
        self.assertTrue(os.path.exists(self.test_file_path_override))
        with open(self.test_file_path_override, "r") as file:
            self.assertEqual(file.read(), self.test_file_override_content)
        
        # check existing file content
        self.assertTrue(os.path.exists(self.test_file_path))
        with open(self.test_file_path, "r") as file:
            self.assertEqual(file.read(), self.test_file_content)

    def test_write_no_open_file(self):
        with self.assertRaises(NoOpenFileError):
            self.writer.write(self.test_file_content)

    def tearDown(self) -> None:
        # after test clean up
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.test_file_path_override):
            os.remove(self.test_file_path_override)
        

    

    
