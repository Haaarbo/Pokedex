from ipok import IPokemon
from random import randint

class PFogo(IPokemon):
    def __init__(self) -> None:
        self.__vida = randint(10, 20)
        self.__elemento = 'Fogo'
        
    def get_elemento(self) -> str:
        return self.__elemento

   # def get_vida(self) -> int:
    #    return self.__vida
    
    def atk1(self) -> int:
        return 5

    def atk2(self) -> int:
        return 3

    def atk3(self) -> int:
        return 6

    