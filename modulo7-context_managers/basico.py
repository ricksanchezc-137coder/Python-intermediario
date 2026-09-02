class MeuContexto:
    def __enter__(self):
        print("Entrando")
        return "valor do enter"
    def __exit__(self, exc_type, exc_value, traceback):
        print("saindo")
        if exc_type is not None:
            print(f"excecao capturada: {exc_type.__name__} - {exc_value}")
        return True

with MeuContexto() as valor:
    print(f"dentro do bloco, valor recebido: {valor}")
    raise ValueError("deu ruim")
