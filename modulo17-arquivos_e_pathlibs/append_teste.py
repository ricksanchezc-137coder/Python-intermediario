from pathlib import Path

caminho = Path("append.txt")

caminho.write_text("linha1\n")
print("depois do 1⁰ write_text")
print(caminho.read_text())

caminho.write_text("linha2\n")
print("depois do 2⁰ write_text")
print(caminho.read_text())

with open(caminho, "a") as f:
    f.write("linha3\n")
print("depois do append:")
print(caminho.read_text())
