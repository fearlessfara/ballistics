#
# Name: sim.py
# Author: Faraone Christian Gennaro
# Version: 1.0
# Copyright: None, (do whatever you want)
# Technology Description: Just a try of performing a simple ballistical simulationù
#
from model import *


def main():
    print("Simulazione Colpo Balistico")
    print("Accelerazione gravitazionale: " + str(GRAVITY_FORCE))

    h0 = float(input("Altezza iniziale (m): "))
    v0 = float(input("Velocità iniziale (m/s): "))
    alpha = float(input("Angolazione lancio (gradi): "))
    calibro = float(input("Calibro (diametro colpo in mm): "))
    peso = float(input("Peso proiettile (g): "))
    print("TIPO PROIETTILE")
    print("tipo 1: proiettili appuntiti (militare)")
    print("tipo 2: proiettili pistole, rivoltella")
    print("tipo 3: proiettili cilindrici (wad cutter)")
    print("tipo 4: proiettili irregolari")
    tipo_proiettile = int(input("tipo: "))

    parabolic(v0, h0, alpha, calibro, peso, tipo_proiettile)


if __name__ == "__main__":
    main()
