
class Carta(object):  # ABSTRACTA (NO EXISTE EN LA VIDA REAL)
    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        super().__init__()
        self.__numero = numero
        self.__palo = palo
        self.__tapada = tapada

    def getnumero(self) -> int:
        return self.__numero

    def getpalo(self) -> int:
        return self.__palo

    def istapada(self) -> bool:
        return self.__tapada

    def setnumero(self, numero: int) -> None:
        self.__numero = numero

    def setpalo(self, palo: int) -> None:
        self.__palo = palo

    def tapar(self) -> None:
        self.__tapada = True

    def destapar(self) -> None:
        self.__tapada = False

    def __str__(self) -> str:
        return f"[{self.dibujonumero()}{self.dibujopalo()}]"

    def isfigura(self) -> bool:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UNA CARTA!")

    def dibujonumero(self) -> str:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UNA CARTA!")

    def dibujopalo(self) -> str:
        raise RuntimeError("ERROR: NO SE PUEDE INSTANCIAR UNA CARTA!")


class Cartapoker(Carta):
    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        super().__init__(numero, palo, tapada=tapada)

    def getcolor(self) -> str:
        if self.getpalo() > 2:
            color = "Negro"
        else:
            color = "Rojo"

    def isfigura(self) -> bool:
        return self.getnumero() > 10

    def dibujonumero(self) -> str:
        numeros = ("#", "A", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K")
        if self.istapada():
            dibujo = numeros[0]
        else:
            dibujo = numeros[self.getnumero()]
        return dibujo

    def dibujopalo(self) -> str:
        palos = ("#", "♥", "♦", "♣", "♠")
        if self.istapada():
            dibujo = palos[0]
        else:
            dibujo = palos[self.getpalo()]
        return dibujo


def main():


    print("\nESTE MODULO NO SE COMPILA\n")


if __name__ == "__main__":
    main()
