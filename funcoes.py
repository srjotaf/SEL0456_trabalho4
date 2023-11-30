import json

class number:
    def __init__(self,n) -> None:
        self.n = n
        self.fat = 1
        self.fib_anterior = 0
        self.fib = 1
        if self.n < 1:
            self.fib = 0
        self.calc_fib()
        self.calc_fat()

    def calc_fat(self):
        i = self.n
        while i > 1:
            self.fat = self.fat*i 
            i -= 1

    def calc_fib(self):
        n = 1
        while n < self.n:
            tmp = self.fib
            self.fib += self.fib_anterior
            self.fib_anterior = tmp
            n += 1

# num = number(5)
# num_json=json.dumps(num.__dict__)

# print(num_json)