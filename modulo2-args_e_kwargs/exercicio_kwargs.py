def mostrar_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

mostrar_kwargs(nome="joao", idade=30)
mostrar_kwargs(x=1)
mostrar_kwargs()

