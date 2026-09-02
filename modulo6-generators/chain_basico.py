import itertools

nomes = ["Ana", "Bruno"]
idades = [30, 25]
junto = itertools.chain(nomes, idades)

print(list(junto))
