# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

a = float(input("Введите число"))
b = float(input("Введите число"))
c = float(input("Введите число"))

result = b ** 2 - 4 * a * c

x1 = (-b + result ** 0.5) / (2 * a)
x2 = (-b - result ** 0.5) / (2 * a)
print(x1, x2)