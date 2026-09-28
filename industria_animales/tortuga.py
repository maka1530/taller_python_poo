from animal import Animal


class Tortuga(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "laguna", "plantas", tamano, color)

    def moverse(self):
        return f"{self.nombre} camina lentamente y nada"

    def adaptacion(self):
        return f"{self.nombre} se protege dentro de su caparazon"
