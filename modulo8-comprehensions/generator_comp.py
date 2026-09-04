numeros = [1, 2, 3, 4, 5]
quadrados_lista = [n**2 for n in numeros]
print(quadrados_lista)

quadrados_gen = (n**2 for n in numeros)
print(quadrados_gen)


print(list(quadrados_gen))
print(quadrados_gen)
print(list(quadrados_gen))
