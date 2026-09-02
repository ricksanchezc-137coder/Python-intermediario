from functools import reduce

numeros = [3, 7, 2, 9, 4]
maior = reduce(lambda acc, x: acc if acc > x else x, numeros)
print(maior)

palavras= ["python", "e", "top"]
frase = reduce(lambda acc, x: acc + " " + x, palavras)
print(frase)
