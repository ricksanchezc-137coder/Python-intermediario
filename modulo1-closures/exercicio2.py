def criar_conta(saldo_inicial):
    def depositar(valor):
        nonlocal saldo_inicial
        saldo_inicial += valor        
    def consultar_saldo():
        return saldo_inicial
    def sacar(valor):
        nonlocal saldo_inicial
        if valor >= saldo_inicial: 
            return f"Saque maior que saldo"
        saldo_inicial -= valor
        return saldo_inicial


    return depositar, consultar_saldo, sacar

depositar, consultar_saldo, sacar = criar_conta(100)

print(consultar_saldo())
depositar(50)
print(consultar_saldo())
depositar(30)
print(consultar_saldo())
print(sacar(30))
print(sacar(1000))
print(consultar_saldo())
