class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f" oi, eu sou {self.nome} e tenho {self.idade} anos"

    @classmethod
    def de_ano_nascimento(cls, nome, ano_nascimento):
        idade = 2026 - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def eh_maior_idade(idade):
        return idade >= 18

p1 = Pessoa("Joao", 25)
#print(p1.apresentar())

p2 = Pessoa.de_ano_nascimento("Maria", 2001)
#print(p2.apresentar())

print(Pessoa.eh_maior_idade(15))
print(Pessoa.eh_maior_idade(25))
