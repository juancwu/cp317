from src.app.formatter import Formatter
from src.app.writer import Writer
from src.app.reader import Reader
from src.app.exceptions import MissingValueError, IncorrectDataTypeError
import unittest
import os
import sys

class FormatterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.formatter = Formatter()
        self.reader = Reader()
        self.writer = Writer()
        self.test_name_file = "tests/data/NameFile.txt"
        self.test_course_file = "tests/data/CourseFile.txt"
        self.formatted_data = "tests/data/FormattedData.txt"
        self.valid_name_data = "150295440, Abdurrahman Person"
        self.invalid_name_datas = [
            "12314adas, Abdurrahman Person", # invalid id
            "150295440, Abda23312", # invalid name
            "1231241234124123123, Abdurrahman Person" # invalid id
        ]
        self.missing_name_datas = [
            "150295440, Abdurrahman Person John", # too many values
            "150295440", # missing name
            "Abdurrahman Person", # missing id
        ]
        self.valid_course_data = "440254806, BU415, 70, 89, 90, 63"
        self.invalid_course_datas = [
            "440254806, BU415, 70, 89, 90, 6a", # invalid grade
            "4402548061111111111111, BU415, 70, 89, 90, 60", # invalid grade
            "440254806, BUA15, 70, 89, 90, 63", # invalid course code
            "440254aa6, BU115, 70, 89, 90, 63", # invalid student id
        ]
        self.missing_course_datas = [
            "440254806, BU415, 70, 89, 90", # missing grade
            "440254806, 70, 89, 90", # missing course
            "440254806, BU415, 70, 89, 90, 63, 70, 89, 90, 63", # too many grades
        ]

    
        super().setUp()

    def tearDown(self) -> None:
        self.formatter = None
        self.reader = None
        self.writer = None
        self.test_name_file = None
        self.test_course_file = None
        self.formatted_data = None
        super().tearDown()
    
    def test_format(self):
        # load name data
        self.reader.open_file(self.test_name_file, "r")
        line = self.reader.read()
        count = 1
        while line:
            self.formatter.load_name_data(line, count)
            line = self.reader.read()
            count += 1
        self.reader.close_file()

        # load course data
        self.reader.open_file(self.test_course_file, "r")
        line = self.reader.read()
        count = 1
        while line:
            self.formatter.load_course_data(line, count)
            line = self.reader.read()
            count += 1
        self.reader.close_file()

        # format data
        formatted_data = self.formatter.format()

        self.assertTrue(len(formatted_data) > 0)

        # check againts valid file
        with open(self.formatted_data, "r") as file:
            valid_data = file.read()
            self.assertEqual(valid_data, formatted_data)
        