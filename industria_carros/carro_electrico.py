from carro import Carro


class CarroElectrico(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "electricidad")

    def sistema_direccion(self, tipo):
        return f"La direccion {tipo} responde de manera silenciosa"

    def tipo_seguridad(self):
        return "Bateria protegida, airbags y frenos ABS"
