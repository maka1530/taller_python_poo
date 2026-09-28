from animal import Animal


class Perro(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "casa y parque", "concentrado", tamano, color)

    def moverse(self):
        return f"{self.nombre} corre por el parque"

    def comunicacion(self):
        return f"{self.nombre} ladra para comunicarse"
