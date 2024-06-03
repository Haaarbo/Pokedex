from abc import ABC, abstractmethod
from random import randint

class IPokemon(ABC):
    @abstractmethod
    def atk1(self):
        pass

    @abstractmethod
    def atk2(self):
        pass

    @abstractmethod
    def atk3(self):
        pass

    def show_vida(self):
        self.vida = randint(10, 19)
        return self.vida
    
    def set_vida(self):
        self.vida
  