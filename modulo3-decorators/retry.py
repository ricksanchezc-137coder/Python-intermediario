import functools 

def tentativas(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Tentativa {i} falhou: {e}")
            raise Exception(f"Todas as {n} tentativas falharam")
        return wrapper
    return decorator

contador = 0

@tentativas(3)
def operacao_instavel():
    global contador
    contador += 1
    if contador < 3:
        raise ValueError("falhou")
    return "sucesso!"

print(operacao_instavel())
