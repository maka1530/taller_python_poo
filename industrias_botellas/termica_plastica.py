from botella_termica import BotellaTermica


class TermicaPlastica(BotellaTermica):
    def __init__(self, capacidad, forma, diseno, tapa, grabados):
        super().__init__("plastico", capacidad, forma, diseno, tapa, grabados)

    def uso_en_bebidas(self, temperatura):
        return f"La botella plastica es adecuada para bebidas {temperatura}"

    def se_ve_el_liquido(self):
        return "En el plastico opaco no se puede observar el liquido"
