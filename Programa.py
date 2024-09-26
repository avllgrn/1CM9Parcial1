import os

def areaRectangulo(base, altura):
    a = base * altura
    return a

def perimetroRectangulo(base, altura):
    p = 2*base + 2*altura
    return p

if __name__ == '__main__':
    os.system('cls')

    base = float(input('Ingresa base '))
    altura = float(input('Ingresa altura '))
    area = areaRectangulo(base, altura)
    perimetro = perimetroRectangulo(base, altura)

    print(f'base = {base}')
    print(f'altura = {altura}')
    print(f'area = {area}')
    print(f'perimetro = {perimetro}')
