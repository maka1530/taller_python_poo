from animal import Animal


class Aguila(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "montana", "carne", tamano, color)

    def moverse(self):
        return f"{self.nombre} vuela muy alto con sus alas"

    def instintos(self):
        return f"{self.nombre} observa a su presa desde el cielo"
