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

    print('1. Convertir a radianes')
    print('2. Seno')
    print('3. Coseno')
    print('4. Tangente')
    opcion = input('Ingresa tu opcion ')

    match opcion:
        case '1':
            grados = float(input('Ingresa grados '))
            radianes = convierteGradosARadianes(grados)
            print(f'{grados}° = {radianes} rads')
        case '2':
            grados = float(input('Ingresa grados '))
            print(f'seno({grados}) = {seno(grados)}')
        case '3':
            grados = float(input('Ingresa grados '))
            print(f'coseno({grados}) = {coseno(grados)}')
        case '4':
            grados = float(input('Ingresa grados '))
            print(f'tangente({grados}) = {tangente(grados)}')
