# Módulo 17 — Arquivos e pathlib

## O que foi feito
Exercícios práticos com `pathlib.Path`: leitura/escrita de texto, navegação de
caminho (name, parent, resolve), criação de diretório e listagem de arquivos
(iterdir, glob), comparação direta com `os.path`, e teste do comportamento de
sobrescrita vs. append.

## O que foi visto no módulo
- `Path` como objeto de caminho, com operador `/` pra montar caminhos
- `read_text()` / `write_text()` como atalhos de leitura/escrita
- `open(caminho, "a")` como única forma de acrescentar sem sobrescrever
- Métodos de navegação: `name`, `stem`, `suffix`, `parent`, `resolve()`
- Operações de diretório: `mkdir(exist_ok=True)`, `iterdir()`, `glob()`
- Equivalência funcional entre `pathlib` e `os.path`

## O que foi aprendido
`write_text()` sempre sobrescreve o arquivo inteiro — não existe "append" no
pathlib puro. `iterdir()` e `glob()` retornam objetos `Path`, não strings.
