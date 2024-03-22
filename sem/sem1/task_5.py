# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.

num = int(input("Input number: "))
for i in range(1, 100):
    if i % num != 0:
        print(i)

