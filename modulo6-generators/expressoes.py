quadrados_lista = [x**2 for x in range(5)]
quadrados_gerador = (x**2 for x in range(5))

print(type(quadrados_lista))
print(type(quadrados_gerador))
print(quadrados_lista)
print(quadrados_gerador)
