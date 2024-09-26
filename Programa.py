import os
import math

def convierteGradosARadianes(grados):
    return grados*math.pi/180

def convierteRadianesAGrados(radianes):
    return radianes*180/math.pi

if __name__ == '__main__':
    os.system('cls')

    xGrados = float(input('Ingresa grados '))    
    xRadianes = convierteGradosARadianes(xGrados)
    print(f'{xGrados}° = {xRadianes} Rads')

    xRadianes = float(input('Ingresa radianes '))
    xGrados = convierteRadianesAGrados(xRadianes)
    print(f'{xRadianes}° = {xGrados} Rads')
