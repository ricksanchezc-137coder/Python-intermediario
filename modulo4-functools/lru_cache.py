import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

inicio = time.perf_counter()
print(fibonacci(35))
print(f"Tempo: {time.perf_counter() - inicio:.4f}s")
print(fibonacci.cache_info())
