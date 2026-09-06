class ContaBancaria:
    taxa_manutencao = 12.0
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        self.saldo += valor

    @classmethod
    def conta_zerada(cls, titular):
        return cls(titular, 0)

    @staticmethod
    def valor_valido(valor):
        return valor > 0


c1 = ContaBancaria("Ana", 100)
c2 = ContaBancaria.conta_zerada("Bruno")

print(c1.titular, c1.saldo)
print(c2.titular, c2.saldo)

print(ContaBancaria.valor_valido(50))
print(ContaBancaria.valor_valido(-10))
