# Рассчитать площадь фигуры по выбору пользователя
import math

print("1-прямоугольник, 2-треугольник, 3-круг")
figure = input("Выберите фигуру: ")

if figure == "1":
    a = float(input("длина = "))
    b = float(input("ширина = "))
    print("Площадь: %.2f" % (a * b))
elif figure == "2":
    a = float(input("сторона a = "))
    b = float(input("сторона b = "))
    c = float(input("сторона c = "))
    P = (a + b + c) / 2
    S = math.sqrt(P * (P - a) * (P - b) * (P - c))
    print("Площадь: %.2f" % S)
elif figure == "3":
    r = float(input("Радиус круга R= "))
    print("Площадь: %.2f" % (math.pi * r ** 2))
else:
    print("Ошибка ввода")
