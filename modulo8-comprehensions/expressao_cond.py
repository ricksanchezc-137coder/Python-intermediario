numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
palavra =[]

for n in numeros:
    if n % 2 == 0:
        n = "par"
    else:
        n = "impar"
    palavra.append(n)
print(palavra)

cond =["par" if n % 2 == 0 else "impar" for n in numeros]
print(cond)



cond_dobro= [n*2 if n % 2 == 0 else n for n in numeros if n > 3]
print(cond_dobro)
