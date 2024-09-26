import os

def areaCuadro(lado):
    a = lado*lado
    return a

def perimetroCuadro(lado):
    p = 4*lado
    return p

if __name__ == '__main__':
    os.system('cls')

    lado = int(input('Ingresa lado '))
    area = areaCuadro(lado)
    perimetro = perimetroCuadro(lado)

    print(f'lado = {lado}')
    print(f'area = {area}')
    print(f'perimetro = {perimetro}')
