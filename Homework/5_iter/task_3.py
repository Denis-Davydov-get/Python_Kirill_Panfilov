'''
Создайте функцию генератор чисел Фибоначчи fibonacci.
Input:
f = fibonacci()
for i in range(10):
    print(next(f))
Output:
0
1
1
2
3
5
8
13
21
34
'''
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b