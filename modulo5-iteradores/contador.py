lista=[1, 2, 3, 4, 5]

for x in lista:
    print(x)

class Contador:
    def __init__(self, inicio, fim):
        self.atual = inicio
        self.fim = fim
    def __iter__(self):
        return self

    def __next__(self):
        if self.atual >= self.fim:
            raise StopIteration
        valor = self.atual
        self.atual +=1
        return valor


for x in Contador(5, 10):
    print(x)

c = Contador(10, 13)
it = iter(c)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
