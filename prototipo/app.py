from Controladores.ControladorEventos import ControladorEventos
from Controladores.ControladorMenus import ControladorMenus
from Controladores.ControladorMapas import ControladorMapas
from Jogo import Jogo
from Mapa.Mapa import Mapa

controladorEventos = ControladorEventos()
controladorMapas = ControladorMapas() 
controladorMenus = ControladorMenus()

mapa = Mapa()
controladorMapas.inclui_mapa(mapa)

jogo = Jogo(
        controlador_eventos= controladorEventos, 
        controlador_mapas= controladorMapas, 
        controlador_menus= controladorMenus
        )

jogo.iniciar()