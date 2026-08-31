funcoes = []
for i in range(3):
    def f(i=i):
        return i
    funcoes.append(f)

resultados=[f() for f in funcoes]
print(resultados)

print(f.__closure__)

