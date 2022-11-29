import unittest
import os
from unittest.mock import patch

# local module
from main import main

class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.name_file = "tests/data/NameFile.txt"
        self.course_file = "tests/data/CourseFile.txt"
        self.output_file = "tests/data/OutputFile.txt"
    
    def tearDown(self) -> None:
        # clean
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
    
    def test_main(self):
        with patch('builtins.input', side_effect=[self.name_file, self.course_file, self.output_file]):
            main()
            self.assertTrue(os.path.exists(self.output_file))
            # check content of output_file agains FormattedData.txt
            with open(self.output_file, "r") as f:
                output = f.read()
            with open("tests/data/FormattedData.txt", "r") as f:
                expected = f.read()
            self.assertEqual(output, expected)
        
    def test_main_quit(self):
        with patch('builtins.input', side_effect=["!q"]):
            main()
            self.assertFalse(os.path.exists(self.output_file))
        
        with patch('builtins.input', side_effect=[self.name_file, "!q"]):
            main()
            self.assertFalse(os.path.exists(self.output_file))

        with patch('builtins.input', side_effect=[self.name_file, self.course_file, "!q"]):
            main()
            self.assertFalse(os.path.exists(self.output_file))\
        
    
    def test_main_invalid_inputs(self):
        # invalid name file
        with patch('builtins.input', side_effect=["invalid", self.course_file, self.output_file]):
            main()
            self.assertFalse(os.path.exists(self.output_file))
        
        # invalid course file
        with patch('builtins.input', side_effect=[self.name_file, "invalid", self.output_file]):
            main()
            self.assertFalse(os.path.exists(self.output_file))

    


