from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from math import cos, sin, radians

g = 9.80665

class Proyectil:


    def __init__(self,v0:float,theta:float,color:str):
        self.x = 0
        self.y = 0
        self.ax = 0
        self.ay = -g
        self.v0 = v0
        self.theta = theta
        self.color = color
        self.vx = v0 * cos(radians(theta))
        self.vy = v0 * sin(radians(theta))


    def __repr__(self):
        return f'({self.x,self.y})'


    def make_path(self,ax):
        self.path, = ax.plot(self.x,self.y,'ro-',color=f'{self.color}', label=f'{self.theta}°/v:{self.v0}')
        self.line, = ax.plot(self.x,self.y,'r--',color=f'{self.color}')


    def set_xy(self,nx,ny):
        self.x = nx
        self.y = ny


    def set_t(self,t):
        self.t = t


    def update_x(self):
        self.x = 0 + self.vx*(self.t) + 0.5*self.ax*((self.t)**2)
        for i in range(1,len(self.y)):
            if self.y[i] == 0:
                self.x[i] = self.x[i-1]


    def update_y(self):
        self.y = 0 + self.vy*(self.t) + 0.5*self.ay*((self.t)**2)
        for i in range(len(self.y)):
            if self.y[i] < 0:
                self.y[i] = 0




    def update_pos(self,frame):
        self.frame = frame
        self.path.set_data((self.x[frame],self.y[frame]))
        self.line.set_data((self.x[:frame],self.y[:frame]))


    def make_some_limits(self):
        t_max = 2*self.v0*sin(radians(self.theta))/g
        y_max = (self.v0*sin(radians(self.theta)))**2 / (2*g)
        x_max = self.v0**2 * sin(2*radians(self.theta))/g

        return t_max,y_max,x_max



def HelloWorld(t_max:float,y_max:float,x_max:float):
    """
    Puede que sea un entorno para simular tiro parabólico y que no
    tengasentimientos (por lo mismo), pero es de buena costumbre saludar. Por
    cierto, está función es donde se configura todo lo relacionado con el plot de
    la animación.
    ====================
        > t_max (float): es el tiempo máximo que dura el proyectil en el aire
        > x_max (float): es la distancia máxima que recorre el proyectil con
            respecto al eje x.
        > y_max (float): es la distancia máxima que recorre el proyectil con
            respecto al eje y.
    ====================
    """
    fig, ax = plt.subplots()
    ax = plt.axes(autoscale_on=True, xlim=(0,x_max*1.4), ylim=(0,y_max*1.4))
    ax.set_xlabel('distancia en x')
    ax.set_ylabel('distancia en y')
    ax.grid()

    t = np.linspace(0,t_max,num=240)
    return fig, ax, t


def MAXMAXMAX(proyectiles):
    MAX_T = 0
    MAX_Y = 0
    MAX_X = 0
    for i in proyectiles:
        t,y,x = i.make_some_limits()
        if t > MAX_T:
            MAX_T = t
        if y > MAX_Y:
            MAX_Y = y
        if x > MAX_X:
            MAX_X = x

    return MAX_T,MAX_Y,MAX_X


def el_alma_de_la_fiesta(frame,tiempo,t_total:int,args:list):

    tiempo.set_text(f'T = {frame/t_total}s')

    for i in args:
        i.update_pos(frame)

    return args




