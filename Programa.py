import os
import math

def formulaGeneralX1(a, b, c):
    discr = math.pow(b, 2) - 4*a*c
    if a==0:
        print('Error! Raíces indeterminadas...')
        return None
    elif discr<0:
        print('Error! Raíces imaginarias...')
        return None
    else:
        x1 = (-b+math.sqrt(discr)) / (2*a)
        return x1

def formulaGeneralX2(a, b, c):
    discr = math.pow(b, 2) - 4*a*c
    if a==0:
        print('Error! Raíces indeterminadas...')
        return None
    elif discr<0:
        print('Error! Raíces imaginarias...')
        return None
    else:
        x2 = (-b-math.sqrt(discr)) / (2*a)
        return x2


if __name__ == '__main__':
    os.system('cls')

    a = float(input('Ingresa a '))
    b = float(input('Ingresa b '))
    c = float(input('Ingresa c '))
    discr = math.pow(b, 2) - 4*a*c

    if a==0:
        print('Error! Raíces indeterminadas...')
    elif discr<0:
        print('Error! Raíces imaginarias...')
    else:
        x1 = formulaGeneralX1(a,b,c)
        x2 = formulaGeneralX2(a,b,c)
        print(f'a = {a}')
        print(f'b = {b}')
        print(f'c = {c}')
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
