#
# # Name: model.py
# # Author: Faraone Christian Gennaro
# # Version: 1.0
# # Copyright: None, (do whatever you want)
# # Technology Description: Just a try of performing a simple ballistical simulation
# # in this page is contained the "model" for the simulations
# #

from pylab import *
import matplotlib.pyplot as plt
import math

GRAVITY_FORCE = 9.80665  # m/s**2


def parabolic(v0, h0, alphag, calibro_mm, tipo_proiettile, peso):
    alpha = math.radians(alphag)
    tempo_volo = (2 * v0 * sin(alpha) / GRAVITY_FORCE)
    gittata_teorica = (2 * (v0 * v0) * cos(alpha) * sin(alpha)) / GRAVITY_FORCE
    altezza_max = ((v0 * v0) * (sin(alpha) * sin(alpha))) / 2 * GRAVITY_FORCE

    c = calibro_mm

    # tipo 1: proiettili appuntiti (militare)
    # tipo 2: proiettili pistole, rivoltella
    # tipo 3: proiettili cilindrici (wad cutter)

    i = 0.8

    if tipo_proiettile == 1:
        i = 0.44
    elif tipo_proiettile == 2:
        i = 1.1
    elif tipo_proiettile == 3:
        i = 3.5
    elif tipo_proiettile == 4:
        i = 4

    coeff_balistico = (c * c * pi * i) / 40000
    print("Coeff. Balistico: " + str(coeff_balistico))
    # calcolo gittata
    gittata_reale = round(1000 * (0.8 + ((peso * v0 * v0) / (i * 40000 * (c * c)))), 5)
    energia_cinetica = (peso*v0*v0)/(2000*GRAVITY_FORCE)
    energia_colpo = (peso*v0*v0)/2000
    print("Gittata reale: " + str(gittata_reale) + " m")
    print("Gittata teorica (nel vuoto): " + str(gittata_teorica) + " m")
    print("Altezza max teorica (nel vuoto a " + str(alphag) + "°): " + str(altezza_max) + " m")
    print("Tempo di volo teorico (nel vuoto): " + str(tempo_volo) + " s")
    print("Energia cinetica: "+str(energia_cinetica))
    print("Energia colpo in J: "+str(energia_colpo))

    theoric_graph_plotter(v0, h0, alphag)
    # return tempo_volo, gittata_teorica, gittata_reale, altezza_max


def theoric_graph_plotter(v0, h0, alphag):
    g = GRAVITY_FORCE

    # v0 = 10.  # m/s
    alpha = math.radians(alphag)
    # h0 = 10.  # m

    vx = v0 * cos(alpha)
    vy = v0 * sin(alpha)

    tf = (vy + sqrt(vy ** 2 + 2 * g * h0)) / g
    xf = vx * tf

    t = arange(0, tf, 0.01)
    xt = vx * t
    yt = h0 + vy * t - 0.5 * g * t ** 2

    plt.title('Traiettoria')
    # naming the x axis
    plt.ylabel('Altezza (m)')
    # naming the y axis
    plt.xlabel('Distanza (m)')

    plt.plot(xt, yt)
    plt.show()
