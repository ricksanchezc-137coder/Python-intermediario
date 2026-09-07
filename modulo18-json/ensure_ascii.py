import json

pessoa = {"nome": "João", "cidade": "São Paulo"}

print(json.dumps(pessoa))
print(json.dumps(pessoa, ensure_ascii=False))
print(json.dumps(pessoa, indent=2))
