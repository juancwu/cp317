from abstracts.formatter_abstract import FormatterAbstract
from app.exceptions import MissingValueError, IncorrectDataTypeError, MissMatchWarning
from collections import defaultdict
import re

class Formatter(FormatterAbstract):

    """
    Key of the data will be the id and it will have an array for the data to store different data
    the data will format like {id: [student_name, course_code, test1, test2, test3, final_exam]}
    """
    def __init__(self):
        self._name_data = defaultdict(str)
        self._course_data = defaultdict(dict)

    def format(self):
        string_data = ""
        
        for student_id, name in self._name_data.items():
            if student_id not in self._course_data:
                print(self._course_data.keys())
                string_data += f"{student_id} {name}\n"
                print(MissMatchWarning(student_id, "course data file"))
            else:
                for course, data in self._course_data[student_id].items():
                    grade = float(data[0]) * 0.2 + float(data[1]) * 0.2 + float(data[2]) * 0.2 + float(data[3]) * 0.4
                    string_data += f"{student_id} {name} {course} {grade:.1f}\n"

        
        return string_data

    def load_name_data(self, data, line):
        # remove leading and trailing spaces and new line character
        data = data.strip()
        text_arr = data.split(", ")
        line = str(line)
        
        # Check for missing data
        if len(text_arr) < 2:
            raise MissingValueError(line, "name data")
        elif len(text_arr) > 2:
            raise MissingValueError(line, "name data")

        # Check for data type entered
        if text_arr[0].isdigit() == False:
            raise IncorrectDataTypeError(line, "name data")
        
        # Check for the maximum length
        if len(text_arr[0]) > 9 or len(text_arr[1]) > 20:
            raise IncorrectDataTypeError(line, "name data")

        if not re.match(r"[a-zA-Z]+\s+[a-zA-Z]*", text_arr[1]):
            raise IncorrectDataTypeError(line, "name data")
        
        #If all the conditions are met, store the data in name_data dictionary for format to use
        self._name_data[text_arr[0]] = text_arr[1]
        
        return 
    
    def load_course_data(self, data, line):
        # remove new line character
        data = data.strip()
        text_arr = data.split(", ")
        line = str(line)

        # Check for missing data
        if len(text_arr) < 6:
            raise MissingValueError(line, "course data")
        elif len(text_arr) > 6:
            raise MissingValueError(line, "course data")
        
        # Check for student id
        if text_arr[0].isdigit() == False:
            raise IncorrectDataTypeError(line, "course data")

        # Check for course code
        if not re.match(r"[A-Z][A-Z][0-9][0-9][0-9]", text_arr[1]):
            raise IncorrectDataTypeError(line, "course data")

        #Check for maximum length
        if len(text_arr[0]) > 9:
            raise IncorrectDataTypeError(line, "course data")
        
        # Check for test scores
        for i in range(2,6):
            if text_arr[i].isdigit() == False:
                raise IncorrectDataTypeError(line, "course data")
        
        #If all the conditions are met, store the data in name_data dictionary for format to use
        self._course_data[text_arr[0]][text_arr[1]] = text_arr[2:]
        
        return 