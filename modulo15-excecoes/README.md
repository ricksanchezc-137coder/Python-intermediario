# Módulo 15 — Exceções customizadas e encadeamento

## O que foi feito

- Exceção customizada simples herdando de `Exception`
- Captura via `try/except` da exceção customizada
- Exceção com atributos próprios (`__init__` + `super().__init__()`)
- Hierarquia de exceções (classe base + duas exceções filhas)
- `raise ... from` explícito (`__cause__`)
- Encadeamento implícito sem `from` (`__context__`)
- Supressão do encadeamento com `from None`

## O que foi visto no módulo

- Toda exceção herda de `BaseException`; exceções customizadas devem herdar de `Exception`
- Diferença entre `__cause__` (explícito, intencional) e `__context__` (implícito, efeito colateral)
- `from None` suprime completamente o rastro da exceção original no traceback

## O que foi aprendido

- Exceções customizadas permitem distinguir erros de domínio de exceções genéricas do Python
- Hierarquia de exceções dá flexibilidade: capturar pela base pega qualquer erro do domínio, capturar pelo tipo específico permite reação diferenciada
- `raise ... from` é o jeito correto de "traduzir" um erro de baixo nível pra um erro de domínio sem perder o rastro da causa original
