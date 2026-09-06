from enum import Enum

class Status(Enum):
    PENDENTE = 1
    PAGO = 2
    CANCELADO = 3

print(Status.PENDENTE)
print(Status.PENDENTE.name)
print(Status.PENDENTE.value)

for s in Status:
    print(s)

print(Status.PENDENTE == Status.PENDENTE)
print(Status.PENDENTE == 1)


print(Status(2))
print(Status["CANCELADO"])
