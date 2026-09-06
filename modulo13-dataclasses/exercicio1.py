class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

p1 = Produto("Caneta", 2.5, 100)
p2 = Produto("Caneta", 2.5, 100)
print(p1)
print(p1 == p2)

print("""


parte dois

""")

from dataclasses import dataclass

@dataclass
class ProdutoDataclass:
    nome : str
    preco : float
    quantidade : int
p3 = ProdutoDataclass("Caneta", 2.5, 100)
p4 = ProdutoDataclass("Caneta", 2.5, 100)

print(p3)
print(p3 == p4)

