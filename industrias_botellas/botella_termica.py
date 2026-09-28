class BotellaTermica:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def llenar(self, bebida):
        return f"La botella se llena con {bebida}"

    def servir(self):
        return f"La forma {self.forma} permite servir la bebida facilmente"

    def precintar(self):
        return f"La {self.tapa} evita que la bebida se derrame"

    def llevar(self):
        return f"La botella de {self.capacidad} se puede llevar en el bolso"

    def sostener(self):
        return f"Su diseno {self.diseno} permite sostenerla con seguridad"

    def uso_en_bebidas(self, temperatura):
        return f"La botella conserva bebidas {temperatura}"

    def reciclar(self):
        return f"La botella de {self.material} se puede reciclar"

    def se_ve_el_liquido(self):
        return f"El material {self.material} determina si se ve el liquido"
