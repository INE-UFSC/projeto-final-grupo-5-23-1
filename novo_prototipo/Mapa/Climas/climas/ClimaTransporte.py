from Mapa.Climas.interfaces.IClima import IClima


class ClimaTransporte(IClima):

    def __init__(self) -> None:
        super().__init__()
        self.mapa = 'Transporte'