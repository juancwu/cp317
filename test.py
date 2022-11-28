import sys
import os
import unittest

# add source directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
# add tests directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tests'))

# import tests
from tests.exceptions_test import ExceptionsTest
from tests.file_handler_test import FileHandlerTest

# setup test suite
suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTests(loader.loadTestsFromTestCase(ExceptionsTest))
suite.addTests(loader.loadTestsFromTestCase(FileHandlerTest))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

# print results
print(result)
