frases = [
    "python e incrivel",
    "comprehensions sao poderosas",
    "praticar sempre ajuda muito",
]


teste1 = [p for f in frases for p in f.split()]
print(teste1)

teste2 = {p: len(p) for p in teste1 if len(p) > 5}
print(teste2)
