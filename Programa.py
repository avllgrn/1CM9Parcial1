import os

def esCaracterNumerico(c):
    ascii = ord(c)
    if ascii>=48 and ascii<=57:
        return True
    else:
        return False

def esCaracterMayuscula(c):
    ascii = ord(c)
    if ascii>=65 and ascii<=90:
        return True
    else:
        return False

def esCaracterMinuscula(c):
    ascii = ord(c)
    if ascii>=97 and ascii<=122:
        return True
    else:
        return False

def esCaracterLetra(c):
    if esCaracterMayuscula(c) or esCaracterMinuscula(c):
        return True
    else:
        return False

def esCaracterEspecial(c):
    if not esCaracterNumerico(c) and not esCaracterLetra(c):
        return True
    else:
        return False

if __name__ == '__main__':
    os.system('cls')

    caracter = input('Ingresa un solo caracter ')

    if esCaracterNumerico(caracter):
        print(f'{caracter} es numérico.')
    else:
        print(f'{caracter} no es numérico.')

    if esCaracterMayuscula(caracter):
        print(f'{caracter} es mayúscula.')
    else:
        print(f'{caracter} no es mayúscula.')

    if esCaracterMinuscula(caracter):
        print(f'{caracter} es minúscula.')
    else:
        print(f'{caracter} no es minúscula.')

    if esCaracterLetra(caracter):
        print(f'{caracter} es letra.')
    else:
        print(f'{caracter} no es letra.')

    if esCaracterEspecial(caracter):
        print(f'{caracter} es caracter especial.')
    else:
        print(f'{caracter} no es caracter especial.')

