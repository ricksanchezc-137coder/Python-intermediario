from collections import namedtuple

Ponto = namedtuple("Ponto", ["x", "y"])

p1 = Ponto(3, 4)
print(p1)
print(p1.x, p1.y)
print(p1[0], p1[1])

try:
    p1.x = 10
except AttributeError as e:
    print("Erro ao tentar mudar:", e)
p2 = p1._replace(x=10)
print(p1)
print(p2)

