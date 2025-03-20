import math

def ostrougolniy_tr(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('Треугольника не существует. Введите другие значения')
    elif c**2 < a**2 + b**2:
        print('Остроугольный треугольник')
    else:
        print('Не остроугольный треугольник. Введите другие значения')
    pperimetr = (a + b + c) / 2
    S = math.sqrt(pperimetr * (pperimetr - a) * (pperimetr - b) * (pperimetr - c))
    return S

def tupougolniy_tr(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('Треугольника не существует. Введите другие значения')
    elif c**2 > a**2 + b**2:
        print('Тупоугольный треугольник')
    else:
        print('Не тупоугольный треугольник. Введите другие значения')
    pperimetr = (a + b + c) / 2
    S = math.sqrt(pperimetr * (pperimetr - a) * (pperimetr - b) * (pperimetr - c))
    return S

def pryamougolniy_tr(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('Треугольника не существует. Введите другие значения')
    elif c ** 2 == a ** 2 + b ** 2:
        print('Прямоугольный треугольник')
    else:
        print('Не прямоугольный треугольник. Введите другие значения')
    pperimetr = (a + b + c) / 2
    S = math.sqrt(pperimetr * (pperimetr - a) * (pperimetr - b) * (pperimetr - c))
    return S


print(ostrougolniy_tr(5, 3, 4))
print(tupougolniy_tr(6, 5, 9))
print(pryamougolniy_tr(3, 4, 5))
