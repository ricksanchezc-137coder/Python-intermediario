from dataclasses import dataclass

@dataclass(frozen=True)
class Ponto:
    x : int
    y : int

p = Ponto(1, 2)
print(p)
p.x = 10
