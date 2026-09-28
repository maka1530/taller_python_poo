from animal import Animal


class Conejo(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "pradera", "hierba", tamano, color)

    def moverse(self):
        return f"{self.nombre} salta rapidamente por la pradera"

    def comunicacion(self):
        return f"{self.nombre} mueve sus orejas para comunicarse"
