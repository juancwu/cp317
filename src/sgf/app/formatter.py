from ..abstracts.formatter_abstract import FormatterAbstract
from .exceptions import MissingValueError, IncorrectDataTypeError, MissMatchWarning
from collections import defaultdict
import re

class Formatter(FormatterAbstract):
    # Static Variable
    table_header = f'{"Student ID":<10} | {"Name":<20} | {"Course Code":<11} | {"Final Grade":<11}'

    """
    Key of the data will be the id and it will have an array for the data to store different data
    the data will format like {id: [student_name, course_code, test1, test2, test3, final_exam]}
    """
    def __init__(self):
        self._name_data = defaultdict(str)
        self._course_data = defaultdict(dict)

    def format(self):
        """
        Formats the data stored in internal buffers into the format shown below:
        
        
        Student ID | Name                  | Course Code | Final Grade    
        ---------- | --------------------- | ----------- | -----------
        123456789  | AAAAAAAAAAAAAAAAAAAA  | CP222       | 69.0

        Usage: table = formatter.format()
        """
        # this will get the header of the table
        table = self._get_format_str("Student ID", "Name", course_code="Course Code", grade="Final Grade")  
        for student_id, name in self._name_data.items():
            if student_id not in self._course_data:
                table += self._get_format_str(student_id, name)
                print(MissMatchWarning(student_id, "course data file"))
            else:
                for course, data in self._course_data[student_id].items():
                    grade = float(data[0]) * 0.2 + float(data[1]) * 0.2 + float(data[2]) * 0.2 + float(data[3]) * 0.4
                    table += self._get_format_str(student_id, name, course_code=course, grade=f"{grade:.1f}")
        
        return table

    def load_name_data(self, data: str, line: int):
        # remove leading and trailing spaces and new line character
        data = data.strip()
        text_arr = data.split(", ")
        
        # Check for missing data
        if len(text_arr) < 2:
            raise MissingValueError(line, "name data")

        # Check for data type entered
        if text_arr[0].isdigit() == False:
            raise IncorrectDataTypeError(line, "name data")
        
        # Check for the maximum length
        if len(text_arr[0]) > 9 or len(text_arr[1]) > 20:
            raise IncorrectDataTypeError(line, "name data")

        # name should be of the following format only
        # 1. John Smith
        # 2. John
        # 3. John Smith Jr.
        # 4. D'Angelo
        # 5. O-Neil
        if not re.match(r"^[A-Z]'?[- a-zA-Z]+$", text_arr[1]):
            raise IncorrectDataTypeError(line, "name data")
        
        #If all the conditions are met, store the data in name_data dictionary for format to use
        self._name_data[text_arr[0]] = text_arr[1]
        
        return 
    
    def load_course_data(self, data: str, line: int):
        # remove new line character
        data = data.strip()
        text_arr = data.split(", ")

        # Check for missing data
        if len(text_arr) < 6:
            raise MissingValueError(line, "course data")
        
        # Check for student id
        if text_arr[0].isdigit() == False:
            raise IncorrectDataTypeError(line, "course data")

        #Check for maximum length
        if len(text_arr[0]) > 9:
            raise IncorrectDataTypeError(line, "course data")

        # Check for course code
        if not re.match(r"(([A-Z]){2}([0-9]){3})\b", text_arr[1]):
            raise IncorrectDataTypeError(line, "course data")

        # Check for test scores
        for i in range(2,6):
            if text_arr[i].isdigit() == False or float(text_arr[i]) > 100 or float(text_arr[i]) < 0:
                raise IncorrectDataTypeError(line, "course data")
        
        #If all the conditions are met, store the data in name_data dictionary for format to use
        self._course_data[text_arr[0]][text_arr[1]] = text_arr[2:6]
        
        return 

    def _get_format_str(self, student_id: str, name: str, course_code: str = "", grade: str = "", end="\n") -> str:
        dash = '-'
        row_separator = f"| {dash * 10:<10} | {dash * 20:<20} | {dash * 11:<11} | {dash * 11:<11} |{end}"
        string_data = f'| {student_id:<10} | {name:<20} | {course_code:<11} | {grade:<11} |{end}' + row_separator
        return string_data
