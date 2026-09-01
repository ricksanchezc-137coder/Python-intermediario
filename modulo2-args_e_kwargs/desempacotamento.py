def soma(a, b, c):
    return a + b + c 

numeros = [1, 2, 3]
print(soma(*numeros))

def apresentar(nome, idade):
    return f"{nome} tem {idade} anos"
dados = {"nome": "joao", "idade": 30}
print(apresentar(**dados))
