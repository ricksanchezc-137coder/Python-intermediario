import functools

def repetir(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resultado = None
            for _ in range(n):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorator

@repetir(3)
def saudacao(nome):
    print(f"Ola, {nome}!")

saudacao("joao")

print(saudacao.__name__)

