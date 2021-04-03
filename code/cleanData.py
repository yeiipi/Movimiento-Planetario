import json
import math

# ====| D A T O S |==== #


sol_pre = { "nombre":"Sol", "distancia":0, "masa":2*(10**30), 'radio':696340}
mercurio_pre = { "nombre":"Mercurio", "distancia":0.387, "masa":3.3*(10**23), 'radio':4878/2}
venus_pre = { "nombre":"Venus", "distancia":0.723, "masa":4.8*(10**24), 'radio':12104/2 }
tierra_pre = { "nombre":"Tierra", "distancia":1, "masa":5.9*(10**24), 'radio':12756/2 }
marte_pre = { "nombre":"Marte", "distancia":1.523, "masa":6.4*(10**23), 'radio':6790/2 }
jupiter_pre = { "nombre":"Jupiter", "distancia":5.202, "masa":1.9*(10**27), 'radio':142800/2 }
saturno_pre = { "nombre":"Saturno", "distancia":9.539, "masa":5.6*(10**26), 'radio':120536/2 }
urano_pre = { "nombre":"Urano", "distancia":19.18, "masa":8.6*(10**25), 'radio':51118/2 }
neptuno_pre = { "nombre":"Neptuno", "distancia":30.06, "masa":1.0*(10**26), 'radio':49528/2 }
pluton_pre = { "nombre":"Pluton", "distancia":39.44, "masa":1.5*(10**22), 'radio':2274/2 }

planetas = [
    sol_pre,
    mercurio_pre,
    venus_pre,
    tierra_pre,
    marte_pre,
    jupiter_pre,
    saturno_pre,
    urano_pre,
    neptuno_pre,
    pluton_pre,
]

# ====| F U N C I O N E S |==== #


def sec_Tperiodo(s:float):
    """Esta función convierte la únidad de tiempo en terminos de años terrestres."""
    Tperiodo_en_años = 3.15*(10**7)
    return s/Tperiodo_en_años

def kg_MA(kg:float):
    """Esta función convierte la únidad de masa en terminos de la masa del Sol."""
    MA_en_kg = 2*(10**30)
    return kg/MA_en_kg

def m_UA(m:float):
    """Esta función convierte la únidad de distancia en terminos de la distancia entre la Tierra y el Sol."""
    UA_en_m = 1.496*(10**11)
    return m/UA_en_m

def Km_m(km:float):
    m_en_Km = 0.001
    return km/m_en_Km

def velocidad(planeta,G):
    try:
        return (G/planeta['distancia'])**0.5
    except:
        return 0


def periodo(planeta,G):
    try:
        return ((4*(math.pi**2) * (planeta['distancia']**(3)))/(G))**0.5
    except:
        return 0

def energiaTildeEnLaI(planeta,G):
    # print(planeta)
    try:
        a = (G*planeta['masa'])/planeta['distancia']
        b = ((planeta['masa']*G)/(2*planeta['distancia']))
        return -a + b
    except:
        return 0


# ====| R U N  |==== #


def main():

    G = 4*(math.pi**2)
    file = dict()

    # Converción de unidades
    for planeta in planetas:
        planeta['radio'] = m_UA(Km_m(planeta["radio"]))
        planeta["masa"] = kg_MA(planeta["masa"])
    for planeta in planetas:
        planeta['velocidad'] = velocidad(planeta,G)
        planeta['periodo'] = periodo(planeta,G)
        planeta['energia'] = energiaTildeEnLaI(planeta,G)


    file['planetas'] = planetas
    # Constante de gravitción Universal
    # https://en.wikipedia.org/wiki/Gravitational_constant#Orbital_mechanics
    file['G'] = G

    with open('planetas.json','w') as f:
        json.dump(file,f,indent=4)


if __name__ == '__main__':
    main()
