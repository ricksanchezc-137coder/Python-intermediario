## Módulo 5 — Iteradores e o protocolo de iteração

Implementado o protocolo de iteração (`__iter__` / `__next__`) numa classe `Contador` customizada. Validado que `for` consome o iterador automaticamente até o `StopIteration` (silencioso), enquanto chamadas manuais de `next()` sem `try/except` propagam a exceção normalmente.

**Conceitos:** iterável vs. iterador, `iter()`/`next()`, `StopIteration` como sinal de controle de fluxo.
