
# Módulo 19 — Logging

## O que foi feito

- `basico.py`: uso de `basicConfig` (nível padrão vs. `DEBUG` explícito)
- `handler_duplo.py`: console e arquivo com níveis e formatos independentes
- `formatter_custom.py`: atributos extras do formatter (`name`, `filename`, `lineno`, `funcName`)
- `rotativo.py`: `RotatingFileHandler` com rotação por tamanho (`maxBytes`/`backupCount`)
- `manutencao.py`: reescrita da lógica do `manutencao.sh` (bash) em Python, com logging completo (console + arquivo rotativo), trava por PID (`os.kill(pid, 0)`), testes via `subprocess`, limpeza de cache via `pathlib`, backup via `tarfile`

## O que foi visto no módulo

- Níveis de severidade (`DEBUG`/`INFO`/`WARNING`/`ERROR`/`CRITICAL`) como filtro numérico, não decoração
- Arquitetura Logger → Handler → Formatter, cada um com responsabilidade e nível próprios
- `getLogger(__name__)` vs. root logger
- `basicConfig` como atalho limitado a um handler, substituído por configuração manual quando é preciso controle fino
- `RotatingFileHandler` para evitar crescimento infinito do arquivo de log

## O que foi aprendido

- Cada handler filtra de forma independente do nível do logger — o mesmo evento pode aparecer em um destino e não no outro
- `FileHandler`/`RotatingFileHandler` abrem em modo append por padrão — não limpam log antigo já existente, mesmo trocando o mecanismo de geração (bash → Python)
- `os.kill(pid, 0)` é o jeito padrão de checar se um processo existe sem matá-lo — mais confiável que buscar por nome de processo (`pgrep`) pra travas de execução única
- Rotação por tamanho descarta permanentemente o log mais antigo além do `backupCount`, sem arquivamento externo
