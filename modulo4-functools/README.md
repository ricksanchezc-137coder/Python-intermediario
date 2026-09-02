## Módulo 4 — functools essencial (partial, reduce, lru_cache)

Ferramentas do módulo `functools` pra manipular funções como objetos: pré-configurar argumentos, acumular resultados e cachear retornos.

- **`partial.py`** — `partial()` fixando argumentos (`moeda`, `casas_decimais`) numa função de formatação, deixando só `valor` variável.
- **`reduce.py`** — `reduce()` usado pra achar o maior número de uma lista e concatenar strings, sem usar `max()` pronto.
- **`lru_cache.py`** — `@lru_cache` aplicado a um Fibonacci recursivo: `fibonacci(35)` em `0.0001s` graças ao cache dos subproblemas repetidos.
- **`cache_comparativo.py`** — comparação de desempenho com e sem repetição de argumentos: ~36x mais rápido quando há repetição (cache útil) vs. nenhum ganho quando os argumentos são todos únicos (cache inútil).

**Conclusão prática:** `lru_cache` só compensa quando há repetição nos argumentos ao longo do tempo.
