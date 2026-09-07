from pathlib import Path

caminho = Path("teste.txt")
print(caminho.name)
print(caminho.parent)
print(caminho.resolve())

pasta = Path("dados")
pasta.mkdir(exist_ok=True)
(pasta / "a.txt").write_text("arquivo a")
(pasta / "b.py").write_text("# arquivo b")

for item in pasta.iterdir():
    print(item)

print(list(pasta.glob("*.py")))

