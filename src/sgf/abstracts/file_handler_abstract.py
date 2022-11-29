from abc import ABC, abstractmethod

class FileHandlerAbstract(ABC):
    @property
    @abstractmethod
    def is_closed(self):
        pass

    @abstractmethod
    def open_file(self, file_path: str) -> None:
        pass

    @abstractmethod
    def close_file(self) -> None:
        pass