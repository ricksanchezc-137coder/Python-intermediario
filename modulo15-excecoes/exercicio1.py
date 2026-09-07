class ErroContaBancaria(Exception):
    pass

class SaldoInsuficienteError(ErroContaBancaria):
    def __init__(self, saldo, valor_solicitado):
        self.saldo = saldo
        self.valor_solicitado = valor_solicitado
        super().__init__(f"Saldo {saldo} insuficiente para saque de {valor_solicitado}")

class ContaBloqueadaError(ErroContaBancaria):
    pass

def testar(excecao):
    try:
        raise excecao
    except ErroContaBancaria as e:
        print(f"Capturado via classe base: {e}")
def converter_valor(texto):
    try:
        return float(texto)
    except ValueError as e:
        raise SaldoInsuficienteError(saldo=0, valor_solicitado=texto) from e
def testar_contexto():
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError("outro erro, sem from")

def testar_suprimido():
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError("erro limpo, sem rastro") from None

testar_suprimido()
#testar_contexto()
#converter_valor("abc")
#testar(SaldoInsuficienteError(saldo=50, valor_solicitado=200))
#testar(ContaBloqueadaError("conta bloqueada por suspeita de fraude"))

