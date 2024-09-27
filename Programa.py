import os
import math

def convierteGradosARadianes(grados):
    return grados*math.pi/180

def seno(x):
    return math.sin(convierteGradosARadianes(x))

def coseno(x):
    return math.cos(convierteGradosARadianes(x))

def tangente(x):
    return math.tan(convierteGradosARadianes(x))

def tablaDelSeno(ini, fin, inc):
    inc = math.fabs(inc)
    if inc>0:
        print(f'x\t| f(x) = sen(x)\n')
        i = ini
        while i<=fin:
            print(f'{i}\t| {seno(i)}')
            i = i+inc

def tablaDelCoseno(ini, fin, inc):
    inc = math.fabs(inc)
    if inc>0:
        print(f'x\t| f(x) = cosen(x)\n')
        i = ini
        while i<=fin:
            print(f'{i}\t| {coseno(i)}')
            i = i+inc

def tablaDeTangente(ini, fin, inc):
    inc = math.fabs(inc)
    if inc>0:
        print(f'x\t| f(x) = tangente(x)\n')
        i = ini
        while i<=fin:
            print(f'{i}\t| {tangente(i)}')
            i = i+inc

if __name__ == '__main__':
    os.system('cls')

    inicio = float(input('Ingresa inicio '))
    final = float(input('Ingresa final '))
    intervalo = float(input('Ingresa intervalo '))

    tablaDelSeno(inicio, final, intervalo)
    print('\n')

    tablaDelCoseno(inicio, final, intervalo)
    print('\n')

    tablaDeTangente(inicio, final, intervalo)
    print('\n')
