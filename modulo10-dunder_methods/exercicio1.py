class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def __repr__(self):
        return f"Livro({self.titulo!r}, {self.autor!r}, {self.preco!r})"

    def __str__(self):
        return f"{self.titulo}, de {self.autor} (R$ {self.preco:.2f})"

    def __eq__(self, other):
        if not isinstance(other, Livro):
            return NotImplemented
        return self.titulo == other.titulo and self.autor == other.autor

    def __lt__(self, other):
        if not isinstance(other, Livro):
            return NotImplemented
        return self.preco < other.preco

    def __hash__(self):
        return hash((self.titulo, self.autor))




l1 = Livro("Duna", "Frank Herbet", 45.90)
l2 = Livro("1984", "George Orwell", 25.00)
l3 = Livro("O hobbit", "J.R.R Tolkien", 39.90)

livros_set = {l1, l2, l3}

print(len(livros_set))
l4 = Livro("Duna", "Frank Herbet", 999.99)
livros_set2 = {l1, l4}
print(len(livros_set2))
print(l1 == l4)
print(hash(l1) == hash(l4))


#print(l1 < l2)
#print(l2 < l1)
#livros = [l1, l2, l3]
#for l in sorted(livros):
#    print(l)
#print(l1 == l2)
#print(l1 == l3)
#print(l1 == "Duna")
#print(repr(livro))
#print(livro)
#print(str(livro))
