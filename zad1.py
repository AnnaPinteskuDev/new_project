import math

def raznostoronniy_tr(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('Треугольника не существует. Введите другие значения')
    elif a != b != c:
        print('Разносторонний треугольник')
    else:
        print('Не разносторонний треугольник. Введите другие значения')
    pperimetr = (a + b + c) / 2
    S = math.sqrt(pperimetr * (pperimetr - a) * (pperimetr - b) * (pperimetr - c))
    return S
print(raznostoronniy_tr(2, 4, 5))

def ravnobedrenniy_tr(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('Треугольника не существует. Введите другие значения')
    elif a == b or a == c or b == c:
        print('Равнобедренный треугольник')
    else:
        print('Не равнобедренный треугольник. Введите другие значения')
    pperimetr = (a + b + c) / 2
    S = math.sqrt(pperimetr * (pperimetr - a) * (pperimetr - b) * (pperimetr - c))
    return S
print(ravnobedrenniy_tr(5, 5, 8))

def ravnostoronniy_tr(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('Треугольника не существует. Введите другие значения')
    elif a == b == c:
        print('Равносторонний треугольник')
    else:
        print('Не равносторонний треугольник. Введите другие значения')
    pperimetr = (a + b + c) / 2
    S = math.sqrt(pperimetr * (pperimetr - a) * (pperimetr - b) * (pperimetr - c))
    return S
print(ravnostoronniy_tr(7, 7, 7))
