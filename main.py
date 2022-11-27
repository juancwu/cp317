import os
import sys

# add source directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


from src.app.reader import Reader

reader =  Reader()

# reader.open_file('test.txt', 'r')

print(reader.is_closed)