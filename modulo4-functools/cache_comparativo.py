import time
import random
from functools import lru_cache

@lru_cache(maxsize=None)
def processar(x):
    time.sleep(0.0005)
    return x * x
#cenario 1: poucos valores muita repeticao (pool de 5 valores, 200 chamadas)
inicio = time.perf_counter()
for _ in range(200):
    processar(random.choice([1, 2, 3, 4, 5]))
tempo_repetido = time.perf_counter() - inicio
print("Com repeticao:", processar.cache_info())
print(f"Tempo: {tempo_repetido:.4f}s\n")

processar.cache_clear()

#cenario 2: 200 valores unicos, sem repeticao nenhuma
inicio = time.perf_counter()
for i in range(200):
    processar(i)
tempo_unico = time.perf_counter() - inicio
print("Sem repeticao:", processar.cache_info())
print(f"Tempo: {tempo_unico:.4f}s") 
