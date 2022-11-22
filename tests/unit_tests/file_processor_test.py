import unittest
from src.app.file_processor import FileProcessor

class FileProcessorUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.file_processor = FileProcessor()



    def test_open_file(self):
        file_path = 'tests/data/CourseFile.txt'
        file_object = self.file_processor.open_file(file_path)
        self.assertIsNotNone(file_object)
        self.file_processor.close_file(file_object)

unittest.main()