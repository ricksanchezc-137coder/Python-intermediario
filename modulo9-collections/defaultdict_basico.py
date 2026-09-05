palavras = ["abacaxi", "banana", "abelha", "cereja", "batata", "coco"]

#agrupado = {}
#for palavra in palavras:
#    letra = palavra[0]
#    if letra not in agrupado:
#        agrupado[letra] = []
#    agrupado[letra].append(palavra)
#
#print(agrupado)
from collections import defaultdict

agrupado_dd = defaultdict(list)
for palavra in palavras:
    letra = palavra[0]
    agrupado_dd[letra].append(palavra)

print(agrupado_dd)
print(dict(agrupado_dd))

print("Tamanho antes:", len(agrupado_dd))
valor = agrupado_dd["z"]
print("Valor de 'z':", valor)
print("tamanho depois:", len(agrupado_dd))
print(dict(agrupado_dd))
