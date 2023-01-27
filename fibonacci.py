import itertools

i = 1

class Fib:

    class _Fib_iter:
        def __init__(self):
            self.fib = 1
            self.fibp = 1
            self.i = 0

        def __next__(self):
                if self.i < 2:
                    self.i += 1
                    return 1
                else:
                    temp = self.fib
                    self.fib = self.fib + self.fibp
                    self.fibp = temp
                    self.i += 1
                    return self.fib

    def __iter__(self):
        return Fib._Fib_iter()

n = int(input("Введите номер чиала Фибоначчи: "))
f = Fib()

while i <= n:
    for g in itertools.islice(f, n):
        print(f"{i}-ое:", g)
        i += 1