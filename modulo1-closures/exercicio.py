def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar


quadriplo = criar_multiplicador(4)
quintuplo = criar_multiplicador(5)

print(quadriplo(10))
print(quadriplo(100))

print(quintuplo(10))
print(quintuplo(100))
