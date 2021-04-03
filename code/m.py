from fun import *


def main():

    col1 = [ '#e76f51', '#f4a261', '#e9c46a', '#8AB17D', '#2a9d8f', '#264653']
    col2 = [ '#8CB369', '#C0CB77', '#DAC773', '#f4c26f', '#f4a259', '#d87755']
    col3 = [ '#40A98C', '#7FC0AA', '#FFDF73', '#F7A04B', '#F95045', '#D7E661']

    p1 = Proyectil(3,15,col1[0])
    p2 = Proyectil(3,30,col1[1])
    p3 = Proyectil(3,45,col1[2])
    p4 = Proyectil(3,60,col1[3])
    p5 = Proyectil(3,75,col1[4])
    p6 = Proyectil(3,90,col1[5])

    proyectiles = [p1,p2,p3,p4,p5,p6]
    MAX_T,MAX_Y,MAX_X = MAXMAXMAX(proyectiles)

    fig, ax, t = HelloWorld(MAX_T,MAX_Y,MAX_X)


    for i in proyectiles:
        i.set_t(t)
        i.update_y()
        i.update_x()
        i.make_path(ax)

    tiempo = ax.text(0.5,MAX_Y*1.25, "T = 0s")


    anim = animation.FuncAnimation(fig,el_alma_de_la_fiesta,frames=len(t),interval=len(t)/24,fargs=[tiempo,len(t)/24,proyectiles])
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()
