from abc import ABC, abstractmethod

"""
Abstract class for formatter
"""

class FormatterAbstract(ABC):
    @property
    @abstractmethod
    def format(self):
        """
        Output data in a specific format:
        id, name, course code, final grade
        """
        pass

    @abstractmethod
    def load_name_data(self, data: str, line: int):
        """
        Load name data into the formatter
        stored in the format of:
        id, name
        """
        pass

    @abstractmethod
    def load_course_data(self, data: str, line: int):
        """
        Load course data into the formatter
        stored in the format of:
        id, course code, test 1, test 2, test 3, final exam
        """
        pass