from cartas import Carta,Cartapoker
from random import shuffle

class Mazo(object):
    def __init__(self) -> None:
        super().__init__()
        self.__lascartas = []

    def getcartas(self)->list:
        return self.__lascartas

    def setcartas(self,cartas:list)->None:
        self.__lascartas = cartas

    def poner(self,carta:Carta)->None:
        self.__lascartas.append(carta)

    def sacar(self)->Carta:
        return self.__lascartas.pop(0)    

    def ver(self,numerocarta:int)->Carta:
        return self.__lascartas[numerocarta]    

    def isvacio(self)->bool:
        return len(self.__lascartas) == 0

    def tienecartas(self)->bool:
        return not self.isvacio()

    def __len__(self)->int:
        return len(self.__lascartas)

    def mezclar(self)->None:
        return shuffle(self.__lascartas)

    def llenar(self)->None:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UN MAZO!")

    def __str__(self) -> str:
        cadena = ""
        for carta in self.__lascartas:
            cadena += str(carta)
        return cadena

class Mazopoker(Mazo):
    def __init__(self) -> None:
        super().__init__()

    
    def llenar(self)->None:
        for numero in range(1, 14):
            for palo in range(1, 5):
                self.poner(Cartapoker(numero, palo))

class Mazoblackjack(Mazo):
    def __init__(self) -> None:
        super().__init__()

    
    def llenar(self)->None:
        for cant_mazos in range(10):
            for numero in range(1, 14):
                for palo in range(1, 5):
                    self.poner(Cartapoker(numero, palo))

    
        

def main():
    m = Mazopoker()
    print("Vacio: ",m)
    m.llenar()
    print("Lleno: ",m) 
    m.mezclar()
    print("Listo para jugar: ",m)


if __name__ == '__main__':
    main()

