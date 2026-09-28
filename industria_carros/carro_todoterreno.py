from carro import Carro


class CarroTodoterreno(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "diesel")

    def sistema_espejo(self, estado):
        return f"Espejos {estado} para recorrer caminos dificiles"

    def sistema_direccion(self, tipo):
        return f"Direccion {tipo} preparada para terrenos irregulares"
