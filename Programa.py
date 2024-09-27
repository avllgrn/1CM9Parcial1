import os
import math

def contadorAscendente(ini, fin, inc):
    inc = math.fabs(inc)
    if inc>0:
        i = ini
        while i<=fin:
            print(i)
            i = i+inc

def contadorDescendente(ini, fin, dec):
    dec = math.fabs(dec)
    if dec>0:
        i = ini
        while i>=fin:
            print(i)
            i = i-dec

if __name__ == '__main__':
    os.system('cls')

    inicio = float(input('Ingresa inicio '))
    final = float(input('Ingresa final '))
    intervalo = float(input('Ingresa intervalo '))

    if inicio<final:
        contadorAscendente(inicio, final, intervalo)
    else:
        contadorDescendente(inicio, final, intervalo)