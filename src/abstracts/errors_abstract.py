from abc import ABC, abstractmethod

class ReadFromClosedFileErrorAbstract(ABC):
    @abstractmethod
    def __init__(self, file_path: str):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class MissMatchErrorAbstract(ABC):
    @abstractmethod
    def __init__(self, student_id: str, missing_in: str):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class WriteToClosedFileErrorAbstract(ABC):
    @abstractmethod
    def __init__(self, file_path: str):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
