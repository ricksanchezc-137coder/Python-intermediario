from enum import Flag, auto
class Permissao(Flag):
    LER = auto()
    ESCREVER = auto()
    EXECUTAR = auto()
p = Permissao.LER | Permissao.ESCREVER

print(p)
print(Permissao.LER in p)
print(Permissao.EXECUTAR in p)
print(p.value)

for perm in Permissao:
    print(perm.name, perm.value)
