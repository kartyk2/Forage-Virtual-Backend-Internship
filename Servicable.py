from abc import ABC, abstractmethod

class Servicable(ABC):

    """
    Interface to make sure all Car objects have a Servicable interface
    """
    @abstractmethod
    def needs_service(self):
        pass
    
