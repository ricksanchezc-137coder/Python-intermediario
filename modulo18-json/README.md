# Módulo 18 — json (serialização/deserialização)

## O que foi feito

Exercícios práticos cobrindo o módulo `json`: serialização/deserialização básica com `dumps`/`loads`, formatação de saída (`ensure_ascii`, `indent`), leitura e escrita em arquivo com `dump`/`load`, serialização de objeto customizado (`__dict__` e `default=`), tratamento de `JSONDecodeError`, e desserialização para objeto customizado com `object_hook`.

## O que foi visto no módulo

- Diferença entre `dumps`/`loads` (string) e `dump`/`load` (arquivo)
- Mapeamento de tipos entre Python e JSON (com a perda da distinção tuple/list)
- Parâmetros `indent`, `sort_keys` e `ensure_ascii`
- `json.JSONDecodeError` e a exigência de aspas duplas no JSON
- Serialização de objetos customizados via `__dict__` e via `default=`
- Desserialização para objetos customizados via `object_hook`

## O que foi aprendido

- `ensure_ascii=True` (padrão) escapa acentos na saída, mas isso não afeta o dict Python resultante do `loads` — o escape é só uma característica da representação em texto
- Objetos customizados não são serializáveis por padrão; `default=` é mais controlado que `__dict__` quando é preciso excluir campos ou tratar vários tipos
- `object_hook` processa cada `{}` do JSON de dentro para fora, substituindo o dict decodificado pelo retorno da função
- Erro de digitação em `__init__` (faltando um `__`) faz o Python tratar o método como comum em vez de reconhecê-lo como construtor, resultando em `TypeError: takes no arguments` — sintoma que não tem relação óbvia com a causa real
