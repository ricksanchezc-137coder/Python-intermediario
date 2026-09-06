class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("preco nao pode ser negativo")
        self._preco = valor

produto = Produto("Caneta", 10)
print(produto.nome, produto.preco)
print(produto._preco)
