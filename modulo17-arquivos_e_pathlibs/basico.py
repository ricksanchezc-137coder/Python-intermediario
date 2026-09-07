from pathlib import Path

caminho = Path("teste.txt")
caminho.write_text("Linha1\nlinha2\n")

conteudo = caminho.read_text()
print(conteudo)
print(caminho.exists())
print(caminho.is_file())
print(caminho.suffix)
print(caminho.stem)
