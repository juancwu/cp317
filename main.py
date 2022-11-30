import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.app.reader import *
from src.app.writer import *
from src.app.formatter import *
from src.app.file_handler import *

#Variable declaration in this section
name_reader = Reader()
course_reader = Reader()
writer = Writer()
formatter = Formatter()
name = input("Please enter the name of the name file: ")
name_reader.open_file(name, "r")
course = input("Please enter the name of the course file: ")
course_reader.open_file(course, "r")
output = input("Please enter the name of the output file: (leave empty for default value output.txt)") or "output.txt"
writer.open_file(output, "w")

#Starts to read the line from the name_data
print("Data being read from name_data...")
name_string = name_reader.read()
line_count = 1
while name_string != "":
    #Format the string into dictionary that we want
    formatter.load_name_data(name_string,line_count)
    name_string = name_reader.read()
    line_count += 1


#Starts to read the line from the course_data
print("Data being read from coruse_data...")
course_string = course_reader.read()
line_count = 1
while course_string != "":
    #Format the string into dictionary that we want
    formatter.load_course_data(course_string, line_count)
    course_string = course_reader.read()

#Writer trys to write 
print("Data storing in output file")
writer.write(formatter.format())

#Close file
name_reader.close_file()
course_reader.close_file()
writer.close_file()
print("Program finished")