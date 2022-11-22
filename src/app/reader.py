from src.abstracts.reader_abstract import ReaderAbstract
from io import TextIOWrapper

class Reader(ReaderAbstract):
    def read(file):
        #Needs to write down the formatter first
        return

    def open_file(file_path):

        assert file_path, 'No file path provided'
        assert isinstance(file_path, str), 'File path must be a string'
        
        try:
            file_object = open(file_path, 'r')
        except Exception as e:
            print("ERROR (FileProcessor): ", str(e))
            return None
        

        return file_object


    def close_file(file):
        assert file, 'No file object provided'
        assert isinstance(file, TextIOWrapper), 'File object must be a TextIOWrapper'

        file.close()
        return