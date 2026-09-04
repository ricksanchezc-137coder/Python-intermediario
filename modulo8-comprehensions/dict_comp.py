nomes = ["ana", "bruno", "carla", "diego"]

tamanhos = {}
for nome in nomes:
    tamanhos[nome] = len(nome)
print(tamanhos)


tamanhos = {nome: len(nome) for nome in nomes}
print(tamanhos)


numeros = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]

quadrados = {numero: numero**2 for numero in numeros}
print(quadrados)
quadrados_pares = {numero: numero**2 for numero in numeros if numero % 2 == 0}
print(quadrados_pares)
