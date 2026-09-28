from carro import Carro


class CarroTaxi(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina")

    def sistema_ventanas(self, estado):
        return f"Ventanas {estado} para comodidad de los pasajeros"

    def tipo_seguridad(self):
        return "Cinturones, airbags y camara de reversa"
