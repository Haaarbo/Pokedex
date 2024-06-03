from abc import ABC, abstractmethod
from random import randint

class IPokemon(ABC):
    @abstractmethod
    def tipo_elemento(self):
        pass

    @abstractmethod
    def atk1(self):
        pass

    @abstractmethod
    def atk2(self):
        pass

    @abstractmethod
    def atk3(self):
        pass

    