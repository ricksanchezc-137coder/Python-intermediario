import time
import functools

def cronometro(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} levou {fim - inicio:.4f}s")
        return resultado
    return wrapper

@cronometro
def soma(a, b):
    return a + b


print(soma(2, 3))
print(soma.__name__)
