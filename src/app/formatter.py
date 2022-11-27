from src.abstracts.formatter_abstract import Formatter_abstract

class Formatter(Formatter_abstract):

    """
    Key of the data will be the id and it will have an array for the data to store different data
    the data will format like {id: [student_name, course_code, test1, test2, test3, final_exam]}
    """
    dict_data = {}

    def format(self, name_data, course_data):
        string_data = ""

        for key, val in self.dict_data:
            grade = val[2] * 0.2 + val[3]  * 0.2 + val[4] * 0.2 + val[5] * 0.4
            string_data += f"{key} {val[0]} {val[1]} {grade:.2f} \n"

        
        return string_data

    def load_name_data(self, data):
        
        
        return
    
    def load_course_data(self, data):
        
        return