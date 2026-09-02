def filtrar_saques(transacoes):
    for t in transacoes:
        if t["tipo"] == "saque":
            yield t
transacoes = [
    {"tipo": "deposito", "valor": 100},
    {"tipo": "saque", "valor": 50},
    {"tipo": "deposito", "valor": 200},
    {"tipo": "saque", "valor": 30},
]

for saque in filtrar_saques(transacoes):
    print(saque)
