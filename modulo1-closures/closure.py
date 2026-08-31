def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

dobro = criar_multiplicador(2)

print(dobro.__closure__)
print(dobro.__closure__[0].cell_contents)
