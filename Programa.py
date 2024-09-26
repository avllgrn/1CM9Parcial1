import os

def suma(x, y):
    z = x+y
    return z

if __name__ == '__main__':
    os.system('cls')
    
    a = int(input('Ingresa un entero '))
    b = int(input('Ingresa otro entero '))
    c = suma(a, b)
    print(f'{a} + {b} = {c}')