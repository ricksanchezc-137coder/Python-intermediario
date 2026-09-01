def only_kw(a , b, *, c):
    print(a, b, c)

only_kw(1, 2, c=3)
only_kw(1, 2, 3)
