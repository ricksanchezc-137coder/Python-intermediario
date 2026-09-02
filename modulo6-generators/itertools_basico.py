import itertools

contador = itertools.count(10, 2)
primeiros = itertools.islice(contador, 5)

print(list(primeiros))
