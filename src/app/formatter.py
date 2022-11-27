from src.abstracts.formatter_abstract import Formatter_abstract
from exceptions import *
import re

class Formatter(Formatter_abstract):

    """
    Key of the data will be the id and it will have an array for the data to store different data
    the data will format like {id: [student_name, course_code, test1, test2, test3, final_exam]}
    """
    name_data = {}
    course_data = {}

    def format(self):
        string_data = ""
        
        for key, val in self.name_data:
            if key not in self.course_data:
                string_data += f"{key} {val}\n"
                print(MissMatchWarning(key, "name_data file"))
            else:
                grade = self.course[key][2] * 0.2 + self.course[key][3] * 0.2 + self.course[key][4] * 0.2 + self.course[key][4] * 0.4
                string_data += f"{key} {val} {self.course_data[key][1]} {grade:.2f}\n"

        
        return string_data

    def load_name_data(self, data):
        text_arr = data.split(", ")
        
        # Check for missing data
        if len(text_arr) != 2:
            raise Exception(MissingValueError)

        # Check for data type entered
        if text_arr[0].isdigit() == False or text_arr[1].isalpha() == False:
            raise Exception(IncorrectDataTypeError)
        
        # Check for the maximum length
        if len(text_arr[0]) > 9 or len(text_arr[1]) > 20:
            raise Exception(IncorrectDataTypeError)
        
        #If all the conditions are met, store the data in name_data dictionary for format to use
        self.name_data[text_arr[0]] = text_arr[1]
        
        return 
    
    def load_course_data(self, data):
        text_arr = data.split(", ")

        # Check for missing data
        if len(text_arr) != 6:
            raise Exception(MissingValueError)
        
        # Check for student id
        if text_arr[0].isdigit() == False:
            raise Exception(IncorrectDataTypeError)

        # Check for course code
        if not re.match(r"[A-Z][A-Z][0-9][0-9][0-9]", text_arr[1]):
            raise Exception(IncorrectDataTypeError)

        #Check for maximum length
        if len(text_arr[0]) > 9:
            raise Exception(IncorrectDataTypeError)
        
        # Check for test scores
        for i in range(2,6):
            if text_arr[i].isdigit() == False:
                raise Exception(IncorrectDataTypeError)
        
        
        
        #If all the conditions are met, store the data in name_data dictionary for format to use
        self.course_data[text_arr[0]] = [text_arr[1], text_arr[2], text_arr[3], text_arr[4], text_arr[5]]
        
        return 