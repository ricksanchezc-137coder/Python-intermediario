
### Módulo 7 — Context Managers (with, __enter__/__exit__, contextlib)

Estudo do protocolo por trás do `with`: classes com `__enter__`/`__exit__`, o decorator `@contextmanager` (baseado em generator) como alternativa mais enxuta, `contextlib.suppress` e `contextlib.ExitStack`.

Praticado com uma simulação de transação (`Transacao`, via `__enter__`/`__exit__`) que reverte o saldo automaticamente se ocorrer um erro no meio da operação — mesmo princípio de commit/rollback aplicável a operações do sistema-bancario que precisam manter o estado consistente mesmo diante de falhas.
