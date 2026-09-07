import os

caminho_str = os.path.join("dados", "a.txt")
existe = os.path.exists(caminho_str)
nome_sem_txt = os.path.splitext(os.path.basename(caminho_str))[0]

from pathlib import Path
caminho = Path("dados") / "a.txt"
existe = caminho.exists()
nome_sem_ext = caminho.stem

print(caminho_str, existe, nome_sem_txt)
print(caminho, existe, nome_sem_ext)
