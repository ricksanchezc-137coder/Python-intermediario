## Módulo 3 — Decorators

Decorators (`func -> wrapper`), preservação de metadados com `functools.wraps`, e decorators parametrizados (`@repetir(3)`, 3 camadas de função).

- `cronometro.py`: decorator de medição de tempo; demonstrado o problema de identidade (`__name__` virando `wrapper`) e a correção com `functools.wraps`.
- `repetir.py`: decorator com argumento, repete a chamada da função `n` vezes.
- `retry.py`: decorator `tentativas(n)` com `try/except`, repete até obter sucesso — caso de uso prático de retry.

**Status:** concluído.
