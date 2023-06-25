from Mapa.Climas.interfaces.IClima import IClima


class ClimaPlanicie(IClima):

    def __init__(self) -> None:
        super().__init__()
        self.mapa = 'Planicie'