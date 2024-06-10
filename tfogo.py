from ipok import IPokemon
from random import randint

class PFogo(IPokemon):
    def __init__(self) -> None:
        self.__vidaMáxima = randint(10, 20)
        self.__vidaAtual = self.__vidaMáxima
        self.__elemento = 'Fogo'
        self.__pow = randint(1, 10)
    
    #obtém elemento do pókemon
    def get_elemento(self) -> str:
        return self.__elemento

    #retorna vida atual do pókemon
    def get_vida(self) -> int:
        return self.__vidaAtual
    
    #atks possíveis
    #atk1
    def atk1(self) -> int:
        return 5

    #atk2
    def atk2(self) -> int:
        return 3

    #atk3
    def atk3(self) -> int:
        return 6
    
    #obtém nível de poder do pókemon
    def get_pow(self):
        return self.__pow
    
    