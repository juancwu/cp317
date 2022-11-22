from src.abstracts.file_process_abstract import FileProcessorAbstract
from io import TextIOWrapper


class FileProcessor(FileProcessorAbstract):
    def open_file(self, file_path):
        """
        Returns a file object
        Parameters:
            file_path (str): path of the file
        
        Returns:
            file_object (file): file object
        """
        assert file_path, 'No file path provided'
        assert isinstance(file_path, str), 'File path must be a string'
        
        # check if file_path can be accessed or not
        try:
            file_object = open(file_path, 'r')
        except Exception as e:
            print("ERROR (FileProcessor): ", str(e))
            return None
        

        return file_object

    def close_file(self, file_object):
        assert file_object, 'No file object provided'
        assert isinstance(file_object, TextIOWrapper), 'File object must be a TextIOWrapper'

        file_object.close()