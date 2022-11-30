from src.app.formatter import Formatter
from src.app.writer import Writer
from src.app.reader import Reader
from src.app.exceptions import MissingValueError, IncorrectDataTypeError
from tests.colours import *
import unittest
import io
import os

class FormatterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.formatter = Formatter()
        self.reader = Reader()
        self.writer = Writer()
        self.test_name_file = "tests/data/NameFile.txt"
        self.test_course_file = "tests/data/CourseFile.txt"
        self.formatted_data = "tests/data/FormattedData.txt"
        self.sample_output = "tests/data/SampleOutput.txt"
        self.valid_name_data = "150295440, Abdurrahman Person"
    
        super().setUp()

    def tearDown(self) -> None:
        self.formatter = None
        self.reader = None
        self.writer = None

        # remove sample output file
        if os.path.exists(self.sample_output):
            os.remove(self.sample_output)

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

        # write formatted data to sample output file
        self.writer.open_file(self.sample_output, "w")
        self.writer.write(formatted_data)
        self.writer.close_file()

        # compare sample output with formatted data
        self.reader.open_file(self.sample_output, "r")
        sample_output = ""
        line = self.reader.read()
        while line:
            sample_output += line
            line = self.reader.read()
        self.reader.close_file()

        # check if sample output is equal to formatted data
        self.assertEqual(sample_output, formatted_data)

        # check againts valid file
        self.reader.open_file(self.formatted_data, "r")
        formatted_data_valid = ""
        line = self.reader.read()
        while line:
            formatted_data_valid += line
            line = self.reader.read()
        self.reader.close_file()

        # check if both are equal
        self.assertEqual(formatted_data, formatted_data_valid)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_format_missmatch(self, mock_stdout):
        # load valid name data
        self.formatter.load_name_data(self.valid_name_data, 1)

        # load random course data
        self.formatter.load_course_data("123456789, BU415, 70, 89, 90, 63", 1)

        # format data
        self.formatter.format()

        expected_output = f"{YELLOW}WARNING: {RESET}Missing {BLUE}150295440{RESET} in {BLUE}course data file{RESET}"

        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
    
    def test_load_missing_name_data(self):
        data = "123456789" # missing name
        with self.assertRaises(MissingValueError):
            self.formatter.load_name_data(data, 1)
        
    
        data = "John Doe" # missing id
        with self.assertRaises(MissingValueError):
            self.formatter.load_name_data(data, 1)
    
    def test_load_missing_course_data(self):
        data = "123456789, BU415" # missing grades
        with self.assertRaises(MissingValueError):
            self.formatter.load_course_data(data, 1)
        
        # missing id
        data = "BU415, 70, 89, 90, 63"
        with self.assertRaises(MissingValueError):
            self.formatter.load_course_data(data, 1)
        
        # missing course code
        data = "123456789, 70, 89, 90, 63"
        with self.assertRaises(MissingValueError):
            self.formatter.load_course_data(data, 1)
        
    def test_invalid_student_id_course(self):
        # id with letters
        data = "123456789a, BU415, 70, 89, 90, 63"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
        
        # id of length > 9
        data = "12345678910, BU415, 70, 89, 90, 63"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
    def test_invalid_student_id_name(self):
        # id with letters
        data = "123456789a, John Doe"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_name_data(data, 1)
        
        
        # id of length > 9
        data = "12345678910, John Doe"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_name_data(data, 1)

    def test_invalid_course_code(self):
        # course code of all letters
        data = "123456789, BUAAA, 70, 89, 90, 63"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
        # course code of all numbers
        data = "123456789, 12345, 70, 89, 90, 63"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
        # course code of length > 5
        data = "123456789, BU4151, 70, 89, 90, 63"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
        # course code of length < 5
        data = "123456789, BU41, 70, 89, 90, 63"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
    
    def test_invalid_grades(self):
        # grade with letters
        data = "123456789, BU415, 70, 89, 90, 6a"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
        # grade of length > 2
        data = "123456789, BU415, 70, 89, 90, 600"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
        # grade with negative sign
        data = "123456789, BU415, 70, 89, 90, -60"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_course_data(data, 1)
        
    def test_invalid_name(self):
        # name with numbers
        data = "123456789, John 123 Doe"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_name_data(data, 1)
        
        # name with special characters
        data = "123456789, John Doe!"
        with self.assertRaises(IncorrectDataTypeError):
            self.formatter.load_name_data(data, 1)