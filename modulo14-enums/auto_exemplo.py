from enum import Enum , auto

class Cor(Enum):
    VERMELHO = auto()
    VERDE = auto()
    AZUL = auto()

for c in Cor:
    print(c.name, c.value)
