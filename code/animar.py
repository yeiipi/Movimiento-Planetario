from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from IPython.display import HTML
import matplotlib.pyplot as plt
import numpy as np


class Animar3D:
    def __init__(self,lx:float,ly:float,lz:float,planetas,recuadros:int,rps:int):
        self.recuadros = recuadros
        self.rps = rps
        self.nombres = [i.nombre for i in planetas]
        self.posXYZmulti = [i.calc_trayectoria(recuadros) for i in planetas ]



    def __repr__(self):
        msm = f"{' ':>{3}}Animación de {len(self.posXYZmulti)} planetas:\n"
        for nombre in self.nombres:
            msm += f"{'-':>{6}} {nombre}\n"
        msm += f"{' ':>{3}}Recuadros por segundo: {self.rps}\n"
        msm += f"{' ':>{3}}Recuadros: {self.recuadros}\n"
        MSM = f"{' ':>{3}}Cada ciclo de la animación dura {self.recuadros/self.rps} segundos.\n"
        msm += MSM
        ret  = "="*(3+len(MSM))+"\n"
        ret += msm
        ret += "="*(3+len(MSM))+"\n"

        return ret




