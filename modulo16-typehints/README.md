## Módulo 16 — Type hints — introdução

Introdução a `typing`: anotações de tipo (`x: int`, `-> str`) documentam o código mas não são validadas em runtime pelo próprio Python (isso fica pra ferramentas como `mypy`).

- `Optional[X]` (ou `X | None`) pra retornos que podem ser `None`
- `Union[X, Y]` (ou `X | Y`) pra aceitar mais de um tipo
- Generics simples: `List[X]`, `Dict[K, V]`, `Tuple[X, Y]` (ou `list[X]`, `dict[K, V]` a partir do Python 3.9)

Exercícios práticos: função com `Optional` (divisão segura), função com `Union` (formatação de id aceitando int ou str), e duas funções com generics (`List[float]` pra média, `Dict[str, int]` pra contagem de palavras).
