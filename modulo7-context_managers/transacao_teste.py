class Transacao:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self._saldo_backup = None

    def __enter__(self):
        self._saldo_backup = self.saldo
        print(f"transacao iniciada, saldo: {self.saldo}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.saldo = self._saldo_backup
            print(f"erro detectado, revertendo saldo para: {self.saldo}")
        else:
            print(f"transacao confirmada, saldo final: {self.saldo}")
        return True

conta = Transacao(100)
with conta as t:
    t.saldo -= 30
    print(f"saldo durante a transacao: {t.saldo}")
    raise ValueError("saldo insuficiente em outra verificacao")
print(f"saldo depois do with: {conta.saldo}")
