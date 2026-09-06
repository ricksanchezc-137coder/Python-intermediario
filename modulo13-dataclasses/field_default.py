from dataclasses import dataclass, field

@dataclass
class Carrinho:
    dono : str
    itens : list = field(default_factory=list)

c1 = Carrinho("Ana")
c2 = Carrinho("Bruno")

c1.itens.append("caneta")

print(c1)
print(c2)

print(c1.itens is c2.itens)
