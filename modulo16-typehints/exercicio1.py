def dividir(a:float, b:float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

print(dividir(10, 2))
print(dividir(10, 0))
