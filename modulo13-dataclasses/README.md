## Módulo 13 — Dataclasses (@dataclass vs. classe tradicional)

Comparação entre classe tradicional (boilerplate manual de `__init__`/`__repr__`/`__eq__`) e `@dataclass` (gerado automaticamente a partir das type hints).

Praticado:
- `@dataclass` gerando `__repr__` e `__eq__` por valor, vs. classe tradicional comparando por identidade
- `field(default_factory=list)` evitando compartilhamento de valores mutáveis entre instâncias
- `frozen=True` bloqueando reatribuição de campos (`FrozenInstanceError`)
- `__post_init__` pra validação e cálculo de campo derivado (atributo criado fora dos campos declarados não entra no `__repr__`, mas existe normalmente no objeto)

Status: concluído ✅
