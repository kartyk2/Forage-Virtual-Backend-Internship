
from abc import ABC, abstractmethod

class Engine(ABC):

    """
    Interface to make sure all Car Engine have a needs_service interface
    """
    @abstractmethod
    def needs_service(self):
        pass
    