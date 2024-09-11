class Item:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        self.acrescimo = 0
        self.desconto = 0

    def aplicar_acrescimo(self, acrescimo):
        self.acrescimo += acrescimo
        self.valor += acrescimo

    def aplicar_desconto(self, desconto):
        self.desconto += desconto
        self.valor -= desconto

    def __str__(self):
        return f"Código: {self.codigo}, Descrição: {self.descricao}, Valor: {self.valor:.2f}, Acréscimo: {self.acrescimo:.2f}, Desconto: {self.desconto:.2f}"

