def log_chamada(func, *args, **kwargs):
    print(f"Chamando {func.__name__} com args={args} kwargs={kwargs}")
    resultado = func(*args, **kwargs)
    print(f" Resultado: {resultado}")
    return resultado

def multiplicar(a, b):
    return a * b

log_chamada(multiplicar, 3, 4)
log_chamada(multiplicar, a=5, b=6)

