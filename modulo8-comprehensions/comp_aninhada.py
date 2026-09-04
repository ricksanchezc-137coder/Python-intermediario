matriz = [[1, 2, 3 ], [4, 5, 6], [7, 8, 9]]
lista_nova = []
for i in matriz:
    for n in i:
        lista_nova.append(n)
print(lista_nova)

comp = [num for linha in matriz for num in linha]
print(comp)
