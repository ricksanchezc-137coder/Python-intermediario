def combo(a, b, *args, c=10, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("kwargs:", kwargs)

combo(1, 2, 3, 4, 5, c=99, x=1, y=2)
combo(1, 2)

combo(1, 2, 3, 4, 5, 99)
