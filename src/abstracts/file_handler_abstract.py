from abc import ABC, abstractmethod

class FileHandlerAbstract(ABC):
    @property
    @abstractmethod
    def is_closed(self):
        pass

    @abstractmethod
    def open_file(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def close_file(self) -> bool:
        pass