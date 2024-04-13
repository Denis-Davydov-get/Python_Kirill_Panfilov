# —оздайте класс-функцию, который считает факториал числа при вызове экземпл€ра.
# Ёкземпл€р должен запоминать последние k значений.
# ѕараметр k передаЄтс€ при создании экземпл€ра.
# ƒобавьте метод дл€ просмотра ранее вызываемых значений и их факториалов.

import json


class Factorial:
    def __init__(self, k: int) -> None:
        self.k = k
        self._history = []

def __call__(self, value):
    result = 1
    for i in range(1, value + 1):
        result *= i
        self._history.append((value, result))
        self._history = self._history[-self.k:]
        return result

@property
def history(self):
    return self._history

def __enter__(self):
    return self

def __exit__(self, exc_type, exc_val, exc_tb):
    with open('result.json', 'w', encoding='UTF-8') as file:
        json.dump(self._history, file)
