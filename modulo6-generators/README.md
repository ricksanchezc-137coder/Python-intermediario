## Módulo 6 — Generators (yield, generator expressions, itertools)

- `yield`: pausa a função e guarda estado, ao contrário de `return`; avaliação preguiçosa (lazy)
- Generator expressions: `(x for x in ...)` vs list comprehension `[x for x in ...]` — mesma lógica, mas sem calcular tudo de uma vez
- `itertools.count`, `itertools.islice`, `itertools.chain` — ferramentas de iteração preguiçosa da standard library
- Aplicado ao sistema-bancario: filtro de transações via generator (`yield`) em vez de lista, economizando memória em listas grandes
