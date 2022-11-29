import sys
import os
from colorama import Fore

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from .app.reader import Reader
from .app.writer import Writer
from .app.formatter import Formatter
from .app.exceptions import QuitException

def graceflul_exit(exception=None,name_reader:Reader=None,course_reader:Reader=None,writer:Writer=None):
    print(exception)

    # find any opened files
    if name_reader and not name_reader.is_closed():
        print(f"{Fore.RED}Closing name reader...{Fore.RESET}")
        name_reader.close_file()
        
    if course_reader and not course_reader.is_closed():
        print(f"{Fore.RED}Closing course reader...{Fore.RESET}")
        course_reader.close_file()
    
    if writer and not writer.is_closed():
        print(f"{Fore.RED}Closing writer...{Fore.RESET}")
        file_path = writer.get_file_path()
        writer.close_file()
        # should remove output file since it has been closed unexpectedly
        if os.path.exists(file_path):
            os.remove(file_path)
            
    print(Fore.RED + "Quitting the program..." + Fore.RESET)

def main():
    name_reader = Reader()
    course_reader = Reader()
    writer = Writer()
    formatter = Formatter()

    try:
        name_file = input(f"{Fore.RESET}Please enter the name of the name file (!q to quit): {Fore.GREEN}")
        if name_file == "!q":
            raise QuitException()
        name_reader.open_file(name_file, "r")
        
        course_file = input(f"{Fore.RESET}Please enter the name of the course file (!q to quit): {Fore.GREEN}")
        if course_file == "!q":
            raise QuitException()
        course_reader.open_file(course_file, "r")
        
        output_file = input(f"{Fore.RESET}Please enter the name of the output file (leave empty for default value output.txt or !q to quit): {Fore.GREEN}") \
            or "output.txt"
        print(Fore.RESET, end="")
        if output_file == "!q":
            raise QuitException()
        writer.open_file(output_file, "w")

        # Starts to read the line from the name_data
        print(f"Data being read from {Fore.BLUE + name_reader.get_file_path() + Fore.RESET}...")
        name_string = name_reader.read()
        line_count = 1
        while name_string != "":
            #Format the string into dictionary that we want
            formatter.load_name_data(name_string,line_count)
            name_string = name_reader.read()
            line_count += 1

        # Starts to read the line from the course_data
        print(f"Data being read from {Fore.BLUE + course_reader.get_file_path() + Fore.RESET}...")
        course_string = course_reader.read()
        line_count = 1
        while course_string != "":
            #Format the string into dictionary that we want
            formatter.load_course_data(course_string, line_count)
            course_string = course_reader.read()

        # Writer tries to write the data into the output file
        print(f"Data being written to {Fore.BLUE + writer.get_file_path() + Fore.RESET}...")
        writer.write(formatter.format())

        # Close file
        name_reader.close_file()
        course_reader.close_file()
        writer.close_file()
        print(f"{Fore.BLUE}Program finished{Fore.RESET}")
    except KeyboardInterrupt as ki:
        graceflul_exit(exception=ki,name_reader=name_reader,course_reader=course_reader,writer=writer)
    except QuitException as qe:
        graceflul_exit(exception=qe,name_reader=name_reader,course_reader=course_reader,writer=writer)
    except Exception as e:
        graceflul_exit(exception=e,name_reader=name_reader,course_reader=course_reader,writer=writer)

if __name__ == "__main__":
    main()