from functools import partial

def formatar(valor, moeda, casas_decimais):
    return f"{moeda} {valor:.{casas_decimais}f}"

formatar_reais = partial(formatar, moeda="R$", casas_decimais=2)

print(formatar_reais(19.9))
print(formatar_reais(100))

