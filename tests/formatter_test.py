from src.app.formatter import *

format = Formatter()
format.load_name_data("123456789, John Hay")
format.load_name_data("223456789, Mary Smith")
print(format.name_data)

format.load_course_data("306851690, CP460, 74, 98, 76, 52")
format.load_course_data("413787382, CP164, 66, 82, 81, 75")
print(format.course_data)