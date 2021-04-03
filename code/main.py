from planetas import *
from pprint import pprint
from matplotlib.animation as animation


def main():

    lim_esp = 100
    frames = 300
    fps = frames/24

    """
    Index Planetas:
    0) Sol
    1) Mercurio,  2) Venus,    3) Tierra,
    4) Marte,     5) Jupiter,  6) Saturno,
    7) Urano,     8) Neptuno,  9) Pluton.
    """
    planetas_raw,G,mapa_distancia = load_planetas(lim_esp,3,4)

    planetas = []

    for planeta in planetas_raw:
        planetas.append(Planeta(planeta,mapa_distancia,frames,G,0.001))

    for i in planetas:
        i.calc_trayectoria()

    recuadros = MAXMAXMAX(planetas)
    rps = 30
    interval = 1000/rps

    fig = plt.figure(figsize=(12,12))
    ax  = fig.gca(projection='3d')

    ani = animation.FuncAnimation(fig,sys_update,frames=frames,fargs=(planetas),interval=rps)








if __name__ == '__main__':

    main()
