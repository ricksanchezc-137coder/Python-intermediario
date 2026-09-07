import json

texto_invalido = "{'nome': 'caneta',  'preco': 3.5}"

try:
    dados = json.loads(texto_invalido)
except json.JSONDecodeError as e:
    print(f"Erro: {e}")

texto_valido = '{"nome": "Caneta", "preco": 3.5}'
dados = json.loads(texto_valido)
print(dados)
