def criar_conta(saldo_inicial):
    def depositar(valor):
        nonlocal saldo_inicial
        saldo_inicial += valor        
    def consultar_saldo():
        return saldo_inicial
    return depositar, consultar_saldo

depositar, consultar_saldo = criar_conta(100)

print(consultar_saldo())
depositar(50)
print(consultar_saldo())
depositar(30)
print(consultar_saldo())

