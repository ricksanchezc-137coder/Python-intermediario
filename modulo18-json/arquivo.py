import json

dados = {"usuario": "joao", "linguagens": ["Python", "Bash"], "ativo": True}

with open("dados.json", "w", encoding="utf-8")as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

with open("dados.json", "r", encoding="utf-8") as f:
    carregado = json.load(f)

print(carregado)
print(type(carregado))
