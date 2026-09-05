### Módulo 9 — collections (defaultdict, Counter, namedtuple, deque)

Estudo do módulo `collections` da biblioteca padrão:

- **defaultdict**: dict que cria valor padrão automaticamente para chaves novas (evita `KeyError`). Atenção: leitura de chave ausente também cria a chave.
- **Counter**: conta ocorrências; `.most_common()` para ranking; suporta soma/subtração entre contagens.
- **namedtuple**: tupla imutável com acesso por nome (`.campo`) além de índice; `._replace()` gera uma cópia alterada.
- **deque**: fila eficiente nas duas pontas (`append`/`appendleft`, `pop`/`popleft`), com `rotate()` e `maxlen` para descarte automático.

Praticado com scripts exploratórios genéricos (agrupamento de palavras, contagem de itens, pontos 2D, histórico com tamanho fixo), sem aplicação direta ao sistema-bancario neste módulo.

**Status:** concluído.
