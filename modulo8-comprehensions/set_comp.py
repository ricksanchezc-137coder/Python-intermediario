palavras = ["gato", "cao", "gato", "peixe", "cao", "gato"]

unicas = set()
for palavra in palavras:
    unicas.add(palavra)

print(unicas)

unicas_comp = {palavra for palavra in palavras}
print(unicas_comp)
