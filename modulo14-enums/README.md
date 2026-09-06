# Módulo 14 — Enums (enum.Enum, Flag, auto())

## O que foi feito

- Criado `basico.py`: `Enum` simples (`Status`) explorando `.name`, `.value`, iteração, comparação por identidade e acesso por valor/nome
- Criado `auto_exemplo.py`: `Enum` (`Cor`) usando `auto()` para gerar valores automaticamente
- Criado `flag_exemplo.py`: `Flag` (`Permissao`) combinando membros com `|` e testando pertencimento com `in`

## O que foi visto no módulo

- `enum.Enum`: cria um tipo com um conjunto fixo e nomeado de valores, evitando strings/números soltos e seus erros de digitação
- Cada membro tem `.name` (nome) e `.value` (valor associado); acesso via `X(valor)` ou `X["NOME"]`
- Comparação em `Enum` é por identidade do membro, não pelo valor bruto (`Status.PENDENTE == 1` é `False`)
- `auto()`: gera valores automaticamente — sequencial (1, 2, 3...) em `Enum` comum
- `Flag`: variante que permite combinar membros com `|` (bitmask); `auto()` aqui gera potências de 2 (1, 2, 4...) em vez de sequencial, porque cada membro precisa ocupar um bit exclusivo

## O que foi aprendido

- `auto()` se comporta diferente dependendo da classe base: sequencial em `Enum`, potências de 2 em `Flag`
- A combinação de `Flag` (`LER | ESCREVER`) funciona porque cada membro ocupa um bit isolado — sem isso, valores colidiriam e a combinação perderia informação
- `Enum` puro não é comparável a valores brutos por padrão (diferente de `IntEnum`, que não foi coberto neste módulo)

## Status

✅ Módulo 14 (Enums) concluído.
