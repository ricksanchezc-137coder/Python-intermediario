from contextlib import suppress, ExitStack

# suppress: ignora um tipo especifico de excecao
with suppress(ZeroDivisionError):
    restultado = 1 / 0
    print("essa linha nunca roda")

print("passou direto, sem traceback")

# ExitStack: abre uma quantidade dinamica de arquivos
nomes = ["a.txt", "b.txt", "c.txt"]
for nome in nomes:
    with open(nome, "w") as f:
        f.write("teste")

with ExitStack() as pilha:
    arquivos = [pilha.enter_context(open(nome)) for nome in nomes]
    print(f"{len(arquivos)} arquivos abertos ao mesmo tempo")
    for arq in arquivos:
        print(arq.read())
