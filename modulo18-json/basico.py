import json

pessoa = {"nome": "João", "idade": 30, "linguagens": ["Python", "Bash"]}

texto = json.dumps(pessoa)
print(texto)
print(type(texto))

de_volta = json.loads(texto)
print(de_volta)
print(type(de_volta))
