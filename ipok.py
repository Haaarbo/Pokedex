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
    
    #função de aplicar algum dano a algo
    def aplicar_dmg(self, vida, dmg):
        return vida - dmg