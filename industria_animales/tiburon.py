from animal import Animal


class Tiburon(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "oceano", "peces", tamano, color)

    def moverse(self):
        return f"{self.nombre} nada velozmente en el oceano"

    def adaptacion(self):
        return f"{self.nombre} se adapta al agua con sus branquias"
