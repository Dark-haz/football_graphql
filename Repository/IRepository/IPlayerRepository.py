
from abc import ABC , abstractmethod

class IPlayerRepository(ABC):
    @abstractmethod
    def getAll():
        pass
    
    @abstractmethod
    def get():
        pass
