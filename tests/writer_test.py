import unittest
import os
import sys
from src import Writer

class WriterTest(unittest.TestCase):
    def setUp(self):
        self.writer = Writer()
        self.cwd = os.getcwd()
        self.test_content = "Hello World!"
        self.test_output_name = "test.txt"
        # self.writer.open_file(os.path.join(self.cwd, self.test_output_name))
    
    # def tearDown(self):
    #     self.writer.close_file()

    def test_open_file(self):
        self.assertTrue(self.writer.open_file(os.path.join(self.cwd, self.test_output_name)))

    def test_write(self):
        self.writer.write(self.test_content)
        self.assertEqual(self.writer._bytes_written, 12)
        self.writer.close_file()
    
    def test_close_file(self):
        self.writer.close_file()
        self.assertFalse(self.writer._file)
    
    def test_write_exception(self):
        self.writer.close_file()
        self.assertFalse(self.writer.write(self.test_content))
    
    def test_check_output_file(self):
        # open the test output file and check its contents
        output_file = open(os.path.join(self.cwd, self.test_output_name), "r")
        output = output_file.readline()
        self.assertIsInstance(output, str)
        self.assertEqual(output, self.test_content)
        output_file.close()

        # delete the test output file
        os.remove(os.path.join(self.cwd, self.test_output_name))



if __name__ == '__main__':
    unittest.main()