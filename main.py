import sys
import os
from colorama import Fore

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.app.reader import Reader
from src.app.writer import Writer
from src.app.formatter import Formatter
from src.app.exceptions import QuitException

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
        
        output_file = input(f"{Fore.RESET}Please enter the name of the output file (leave empty for default value output.txt or !q to quit): {Fore.GREEN}") or "output.txt"
        print(Fore.RESET, end="")
        if output_file == "!q":
            raise QuitException()
        output_file = writer.open_file(output_file, "w")

        # Starts to read the line from the name_data
        print(f"Data being read from {Fore.BLUE + name_file + Fore.RESET}...")
        name_string = name_reader.read()
        line_count = 1
        while name_string != "":
            #Format the string into dictionary that we want
            formatter.load_name_data(name_string,line_count)
            name_string = name_reader.read()
            line_count += 1

        # Starts to read the line from the course_data
        print(f"Data being read from {Fore.BLUE + course_file + Fore.RESET}...")
        course_string = course_reader.read()
        line_count = 1
        while course_string != "":
            #Format the string into dictionary that we want
            formatter.load_course_data(course_string, line_count)
            course_string = course_reader.read()

        # Writer tries to write the data into the output file
        print(f"Data being written to {Fore.BLUE + output_file + Fore.RESET}...")
        writer.write(formatter.format())

        # Close file
        name_reader.close_file()
        course_reader.close_file()
        writer.close_file()
        print(f"{Fore.BLUE}Program finished{Fore.RESET}")
    except QuitException as e:
        # find any opened files
        if name_reader and not name_reader.is_closed():
            print(f"{Fore.RED}Closing name reader...{Fore.RESET}")
            name_reader.close_file()
        if course_reader and not course_reader.is_closed():
            print(f"{Fore.RED}Closing course reader...{Fore.RESET}")
            course_reader.close_file()
        print(e)
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()