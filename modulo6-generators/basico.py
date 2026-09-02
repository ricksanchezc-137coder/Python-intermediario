def contar_ate(n):
    i = 1
    while i <= n:
        yield i
        i += 1


gerador = contar_ate(3)
print(type(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

