import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
import math as m
import json


cmap = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn',
        'Spectral', 'coolwarm', 'bwr', 'seismic']


def load_planetas(lim_esp,*args):

    global cmap

    max_d = 0
    min_d = 0


    info = dict()
    planetas = []

    with open('planetas.json', 'r') as f:
        info = json.load(f)

    G = info['G']

    for i in range(len(args)):
        p = info['planetas'][args[i]]
        p['color'] = cmap[i]
        planetas.append(p)


        if p['distancia'] > max_d:
            max_d = p['distancia']
        elif p['distancia'] < min_d:
            min_d = p['distancia']

    mapa_distancia = interp1d([0,max_d],[0,lim_esp/2])

    return planetas,G,mapa_distancia



class Planeta:
    def __init__(self,raw_info:dict,mapa_distancia,frames,G,delta):

        self.G = G

        self.nombre = raw_info['nombre']
        self.masa = raw_info['masa']
        self.distancia = raw_info['distancia']
        self.color = raw_info['color']
        self.radio = raw_info['radio']

        # Definicion de la figura
        u = np.linspace(0, 2 * np.pi, frames)
        v = np.linspace(0, np.pi, frames)
        t = mapa_distancia(raw_info['radio'])

        self.x = t * np.outer(np.cos(u), np.sin(v))
        self.y = t * np.outer(np.sin(u), np.sin(v))
        self.z = t * np.outer(np.ones(np.size(u)), np.cos(v))


        self.delta = delta

        self.velX  = 0.0
        self.posXa = self.distancia
        self.posXb = self.posXa+self.velX*self.delta
        try:
            self.acelX = -self.G/(self.distancia**3)*self.posXb
        except:
            self.acelX = 0.0

        self.velY  = raw_info['velocidad']
        self.posYa = 0.0
        self.posYb = self.posYa+self.velY*self.delta
        try:
            self.acelY = -self.G/(self.distancia**3)*self.posYb
        except:
            self.acelY = 0.0

        self.posZ = 0.0

    def __repr__(self):
        s = f"\n{self.nombre}"
        s += f": - pos: ( {self.posXb} , {self.posYb} , {self.posZ} )\n"
        s += f"{'-':>{int(len(nombre)+3)}} masa: {self.masa} MA\n"
        s += f"{'-':>{int(len(nombre)+3)}} radio: {self.radio} UA"
        return s

    def update_posicion(self):
        # verlet
        tempX = self.posXb
        tempY = self.posYb
        self.posXb = (2*self.posXb) - self.posXa + (self.acelX*self.delta**2)
        self.posYb = (2*self.posYb) - self.posYa + (self.acelY*self.delta**2)
        self.posXa = tempX
        self.posYa = tempY



    def update_velocidad(self):
        # verlet velocidad
        self.velX = (self.posXb - self.posXa)/(2*self.delta)
        self.velY = (self.posYb - self.posYa)/(2*self.delta)


    def update_aceleracion(self):
        try:
            self.acelX = -self.G/(self.distancia**3)*self.posXb
        except:
            self.acelX = 0.0
        try:
            self.acelY = -self.G/(self.distancia**3)*self.posYb
        except:
            self.acelY = 0.0

    def calc_trayectoria(self):
        self.posXYZ = list()
        self.frames_total = 0
        while True:
            self.posXYZ.append([self.posXb,self.posYb,0.0])
            self.update_aceleracion()
            self.update_posicion()
            self.update_velocidad()
            condx = round(self.posXYZ[0][0],3) == round(self.posXYZ[-1][0],3)
            condy = round(self.posXYZ[0][1],3) == round(self.posXYZ[-1][1],3)

            if condx and condy and (self.frames_total != 0):
                break
            else:
                self.frames_total += 1



def MAXMAXMAX(planetas):
    MAX_R = 0
    for p in planetas:
        if ( p.frames_total > MAX_R ):
            MAX_R = p.frames_total

    return MAX_R




def el_alma_de_la_fiesta(frame,planetas):















