import json

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto(nome={self.nome!r}, preco={self.preco!r})"

def dict_para_produto(d):
    if "nome" in d and "preco" in d:
        return Produto(d["nome"], d["preco"])
    return d

texto = '{"nome": "Caneta", "preco": 3.5}'

comum = json.loads(texto)
print(comum, type(comum))

produto = json.loads(texto, object_hook=dict_para_produto)
print(produto, type(produto))
