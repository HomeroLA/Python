class Direccion():
    def __init__(self, calle: str, altura: str, ubicacion: str,) -> None:
        self.__calle = calle
        self.__altura = altura
        self.__ubicacion = ubicacion

    def setcalle(self, calle: str) -> None:
        self.__calle = calle

    def getcalle(self) -> str:
        return self.__calle

    def setaltura(self, altura: int) -> None:
        self.__altura = altura

    def getaltura(self) -> int:
        return self.__altura

    def setubicacion(self, ubicacion: str) -> None:
        self.__ubicacion = ubicacion

    def getubicacion(self) -> str:
        return self.__ubicacion

    def __str__(self) -> str:
        return f"Dierccion: {self.getcalle()} {self.getaltura()} [{self.getubicacion()}]"

#------------------------------------------------------------------------------
class Persona():
    def __init__(self, nombre: str, sexo: str, edad: int, dni: str,  mail: str, 
                 direccion: Direccion) -> None:
        self.__nombre = nombre
        self.__sexo = sexo
        self.__edad = edad
        self.__dni = dni
        self.__mail = mail
        self.__direccion = direccion

    def setnombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def getnombre(self) -> str:
        return self.__nombre

    def setsexo(self, sexo: str) -> None:
        self.__sexo = sexo

    def getsexo(self) -> str:
        return self.__sexo

    def setedad(self, edad: int) -> None:
        self.__edad = edad

    def getedad(self) -> int:
        return self.__edad

    def setdni(self, dni: str) -> None:
        self.__dni = dni

    def getdni(self) -> str:
        return self.__dni

    def setmail(self, mail: str) -> None:
        self.__mail = mail

    def setdireccion(self, direccion: Direccion) -> None:
        self.__direccion = direccion

    def getdireccion(self) -> Direccion:
        return self.__direccion

    def getmail(self) -> str:
        return self.__mail

    def __str__(self) -> str:
        return f"Dni:{self.getdni()} - Nombre:{self.getnombre():20s}\nSexo:({self.getsexo()})\n{self.getdireccion()}\nMail:{self.getmail()}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, otro: object) -> bool:
        iguales = True
        if not isinstance(otro,Persona):
            iguales = False
        if self.getdni() != otro.getdni():
            iguales = False
        return iguales
        

def main():
    d1 = Direccion('Av. Salta', '3453', 'Puerta Roja Al Fondo')
    p1 = Persona('Juan', 'M', 25, 34567890, d1, 'juan_1234@gmail.com')
    p2 = Persona('Pedro','M',18,'40123123','pp.gmail.com',d1)
    print(p1)
    print(p2)

    a = int(3)
    if p1 == p2:
        print("IGUALES")
    else:
        print("DISTINTOS")
    lista = []
    lista.append(p1)
    lista.append(p2)
    print(lista)

main()
