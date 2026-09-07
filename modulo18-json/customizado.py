import json

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco =  preco

produto = Produto("Caneta", 3.5)

try:
    print(json.dumps(produto))
except TypeError as e:
    print(f"Erro: {e}")

print(json.dumps(produto.__dict__))

def produto_para_dict(obj):
    if isinstance(obj, Produto):
        return {"nome": obj.nome, "preco": obj.preco}
    raise TypeError(f"Objeto do tipo: {type(obj)} nao e serializavel")

print(json.dumps(produto, default=produto_para_dict))
