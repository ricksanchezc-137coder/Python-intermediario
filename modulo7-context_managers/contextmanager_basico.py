from contextlib import contextmanager

@contextmanager
def meu_contexto():
    print("entrando")
    try:
        yield "valor do enter"
    except ValueError as e:
        print(f"excecao capturada: {type(e).__name__} - {e}")
    finally:
        print("saindo")

with meu_contexto() as valor:
    print(f"dentro do bloco, valor recebido: {valor}")
    raise ValueError("deu ruim")
