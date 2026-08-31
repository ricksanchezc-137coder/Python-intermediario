def criar_cache(func):
    cache = {}
    
    def funcao_com_cache(x):
       if x not in cache:
           print(f"Calculando o valor para {x}...")
           resultado = func(x)
           cache[x] = resultado
       return cache[x]
   
    return funcao_com_cache

def quadrado(n):
    print(f"Calculando o quadrado de {n}...")
    return n * n

quadrado_com_cache = criar_cache(quadrado)

print(quadrado_com_cache(5))
print(quadrado_com_cache(5))
print(quadrado_com_cache(10))
print(quadrado_com_cache(5))
