from collections import Counter

palavras = ["gato", "cao", "gato", "peixe", "cao", "gato"]

contagem = Counter(palavras)
#print(contagem)
#print(contagem["gato"])
#print(contagem["hamster"])

#print(len(contagem))
#_ = contagem["hamster"]
#print(len(contagem))
#print(contagem)

print(contagem.most_common())
print(contagem.most_common(2))

outra_contagem = Counter(["gato", "gato", "papagaio"])
print(contagem + outra_contagem)
print(contagem - outra_contagem)

