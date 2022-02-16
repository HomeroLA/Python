from cartas import Carta, Cartapoker
from mazos import Mazo, Mazoblackjack, Mazopoker
from random import randint
from teclado import leerint,leerintrango



class Jugadorcartas(object):
    def __init__(self, nombre: str, mano: Mazo) -> None:
        super().__init__()
        self.__mano = mano
        self.__nombre = nombre

    def getmano(self) -> Mazo:
        return self.__mano

    def getnombre(self) -> str:
        return self.__nombre

    def setmano(self, mano: Mazo) -> None:
        self.__mano = mano

    def setnombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def poner(self, carta: Carta) -> None:
        self.getmano().poner(carta)

    def sacar(self) -> Carta:
        return self.getmano().sacar()

    def tienecartas(self) -> bool:
        return not self.getmano().isvacio()

    def __str__(self) -> str:
        return f"{self.getnombre()} - {str(self.getmano())}"


class Jugadorblackjack(Jugadorcartas):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre, Mazoblackjack())

    def tieneblack(self) -> bool:
        return len(self.getmano()) == 2 and self.sumacartas() == 21

    def sumacartas(self) -> int:
        sumatotal = 0
        sumanumeros = 0
        cantidad_ases = 0
        mazo = self.getmano()
        for x in range(len(mazo)):
            numero = mazo.ver(x).getnumero()
            if numero == 1:
                cantidad_ases += 1
            elif numero > 9:
                sumanumeros += 10
            else:
                sumanumeros += numero
        if cantidad_ases == 0:
            sumatotal = sumanumeros
        elif cantidad_ases == 1:
            if sumanumeros + 11 > 21:
                sumatotal = sumanumeros + 1
            else:
                sumatotal = sumanumeros + 11
        else:
            if sumanumeros + 11 + cantidad_ases - 1 > 21:
                sumatotal = sumanumeros + cantidad_ases
            else:
                sumatotal = sumanumeros + 11 + cantidad_ases - 1
        return sumatotal

    def seplanta(self) -> bool:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UN JUGADORBLACKJACK")


class Croupier(Jugadorblackjack):
    def __init__(self) -> None:
        super().__init__("Sr Croupier")

    def seplanta(self) -> bool:        
        print(str(self),end='')
        suma = self.sumacartas()
        if suma > 21:
            print(f"{'{'}{'SE PASO'}{'}'}")
            respuesta = True
        elif suma > 17:
            print(f"{'{'}{'SE PLANTA'}{'}'}")
            respuesta = True
        else:
            respuesta = False

        return respuesta

    
class Cliente(Jugadorblackjack):
    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre)
        self.__fichas = fichas

    def getfichas(self) -> int:
        return self.__fichas

    def setfichas(self, fichas: int) -> None:
        self.__fichas = fichas

    def ganarfichas(self, fichas: int) -> None:
        self.__fichas += fichas

    def perderfichas(self, fichas: int) -> None:
        self.__fichas -= fichas

    def seplanta(self) -> bool:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UN CLIENTE")

    def seretira(self) -> bool:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UN CLIENTE")

    def apuesta(self) -> int:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UN CLIENTE")

    def __str__(self) -> str:
        return super().__str__() + f" - ({self.sumacartas()}) - <{self.getfichas()}>"


class Computadora(Cliente):
    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre, fichas)
        self.__personalidad = randint(0, 100)

    def __pensar(self) -> int:
        return randint(1, 100)

    
    def seplanta(self) -> bool:
        print(str(self),end='')
        if self.sumacartas() > 21:
            print(f"{'{'}{'SE PASO'}{'}'}")
            respuesta = True
        else:
            print("SE PLANTA? [S/N]: ",end='')
            if self.__pensar() <= self.__personalidad:
                respuesta = True
                cadena =  'S'
            else:
                respuesta = False
                cadena = 'N'
            print(cadena)
        return respuesta

    def seretira(self) -> bool:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UN CLIENTE")

    def apuesta(self) -> int:
        if self.getfichas() == 1:
            cantidad = 1
        elif self.__pensar() <= self.__personalidad:
            cantidad = randint(self.getfichas()//2, self.getfichas())
        else:
            cantidad = randint(1, self.getfichas()//2)
        print(str(self))
        print(f"FICHAS APOSTADAS: {cantidad}")
        return cantidad


class Humano(Cliente):
    def __init__(self, nombre: str, fichas: int) -> None:
        super().__init__(nombre, fichas)

    def seplanta(self) -> bool:
        print(str(self),end='')
        if self.sumacartas() > 21:
            print(f"{'{'}{'SE PASO'}{'}'}")
            respuesta = True
        else:
            respuesta = input("SE PLANTA? [S/N]: ").upper() == 'S'

        return respuesta

    def seretira(self) -> bool:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UN CLIENTE")

    def apuesta(self) -> int:
        print(str(self))
        return leerintrango("FICHAS APOSTADAS: ",1,self.getfichas())
        


def main():

    j1 = Humano("Rosita", 100)
    j1.poner(Cartapoker(2, 1))
    j1.poner(Cartapoker(5, 2))
    j1.poner(Cartapoker(1, 1))
    print(j1)
    j1.poner(Cartapoker(1, 1))
    print(j1)

    jc = Croupier()
    jc.poner(Cartapoker(11, 1, True))
    jc.poner(Cartapoker(1, 3))
    print(jc)


if __name__ == '__main__':
    main()
