from abc import ABC, abstractmethod

class Battery(ABC):

    """
    Interface to make sure all Car Battery have a needs_service interface
    """
    @abstractmethod
    def needs_servicing(self):
        pass
