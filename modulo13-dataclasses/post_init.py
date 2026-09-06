from dataclasses import dataclass

@dataclass
class Retangulo:
    largura : float
    altura : float

    def __post_init__(self):
        if self.largura <= 0 or self.altura <= 0:
            raise ValueError("dimensoes devem ser positivas")
        self.area = self.largura * self.altura

r1 = Retangulo(5, 3)
print(r1)
print(r1.area)

#r2 = Retangulo(-1, 3)
print(r1.__dict__)
