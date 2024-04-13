class Factorial:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step


def __iter__(self):
    return self


def __next__(self):
    self.start += self.step
    while self.start <= self.stop:
        return self.factorial(self.start - self.step)
    raise StopIteration


def factorial(self, num):
    count = 1
    for i in range(1, num + 1):
        count = count * i
        return count


if __name__ == '__main__':
    fact = Factorial(4)
    for n in fact:
        print(n)
