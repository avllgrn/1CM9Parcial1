import os
import math

def convierteGradosARadianes(grados):
    return grados*math.pi/180

def convierteRadianesAGrados(radianes):
    return radianes*180/math.pi

def seno(x):
    return math.sin(convierteGradosARadianes(x))

def coseno(x):
    return math.cos(convierteGradosARadianes(x))

def tangente(x):
    return math.tan(convierteGradosARadianes(x))

if __name__ == '__main__':
    os.system('cls')

    xGrados = float(input('Ingresa grados '))    
    xRadianes = convierteGradosARadianes(xGrados)

    print(f'{xGrados}° = {xRadianes} Rads')
    print(f'seno({xGrados}) = {seno(xGrados)}')
    print(f'coseno({xGrados}) = {coseno(xGrados)}')
    print(f'tangente({xGrados}) = {tangente(xGrados)}')
