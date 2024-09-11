from Item import *
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        if not self.itens:
            print("O carrinho está vazio.")
        else:
            print("Itens no carrinho:")
            for item in self.itens:
                print(item)

    def buscar_item_por_codigo(self, codigo):
        for item in self.itens:
            if item.codigo == codigo:
                return item
        return None

    def aplicar_acrescimo_item(self, codigo, acrescimo):
        item = self.buscar_item_por_codigo(codigo)
        if item:
            item.aplicar_acrescimo(acrescimo)
        else:
            print("Item não encontrado.")

    def aplicar_desconto_item(self, codigo, desconto):
        item = self.buscar_item_por_codigo(codigo)
        if item:
            item.aplicar_desconto(desconto)
        else:
            print("Item não encontrado.")

    def distribuir_acrescimo_total(self, acrescimo_total):
        if len(self.itens) == 0:
            return
        acrescimo_por_item = acrescimo_total / len(self.itens)
        for item in self.itens:
            item.aplicar_acrescimo(acrescimo_por_item)

    def distribuir_desconto_total(self, desconto_total):
        if len(self.itens) == 0:
            return
        desconto_por_item = desconto_total / len(self.itens)
        for item in self.itens:
            item.aplicar_desconto(desconto_por_item)

    def finalizar_venda(self):
        total_acrescimo = sum(item.acrescimo for item in self.itens)
        total_desconto = sum(item.desconto for item in self.itens)
        valor_final = sum(item.valor for item in self.itens)

        print("\nResumo da venda:")
        for item in self.itens:
            print(item)
        print(f"\nAcréscimo total: {total_acrescimo:.2f}")
        print(f"Desconto total: {total_desconto:.2f}")
        print(f"Valor final: {valor_final:.2f}")


def inicializar_itens_predefinidos():
    # Lista com os itens predefinidos
    return [
        {"codigo": "001", "descricao": "Mouse", "valor": 50.0},
        {"codigo": "002", "descricao": "Teclado", "valor": 100.0},
        {"codigo": "003", "descricao": "Monitor", "valor": 750.0},
        {"codigo": "004", "descricao": "Cadeira Gamer", "valor": 500.0},
        {"codigo": "005", "descricao": "Fone de Ouvido", "valor": 150.0},
        {"codigo": "006", "descricao": "Notebook", "valor": 3000.0},
        {"codigo": "007", "descricao": "Impressora", "valor": 200.0}
    ]


def exibir_menu():
    print("\n1. Inserir item ao carrinho")
    print("2. Acréscimo de item")
    print("3. Desconto de item")
    print("4. Acréscimo total")
    print("5. Desconto total")
    print("6. Listar itens do carrinho")
    print("7. Listar itens disponíveis")
    print("8. Finalizar venda")
    print("Escolha uma opção: ", end='')


def inserir_item(carrinho, itens_disponiveis):
    print("\nItens disponíveis para adicionar ao carrinho:")
    for i, item in enumerate(itens_disponiveis, start=1):
        print(f"{i}. {item['descricao']} (Código: {item['codigo']}, Valor: {item['valor']})")

    escolha = int(input("\nEscolha o número do item para adicionar ao carrinho: ")) - 1

    if 0 <= escolha < len(itens_disponiveis):
        item_escolhido = itens_disponiveis[escolha]
        item = Item(item_escolhido["codigo"], item_escolhido["descricao"], item_escolhido["valor"])
        carrinho.adicionar_item(item)
        print(f"\nItem '{item_escolhido['descricao']}' adicionado ao carrinho.")
    else:
        print("Opção inválida!")


def aplicar_acrescimo_item(carrinho):
    codigo = input("Código do item: ")
    acrescimo = float(input("Valor do acréscimo: "))
    carrinho.aplicar_acrescimo_item(codigo, acrescimo)


def aplicar_desconto_item(carrinho):
    codigo = input("Código do item: ")
    desconto = float(input("Valor do desconto: "))
    carrinho.aplicar_desconto_item(codigo, desconto)


def aplicar_acrescimo_total(carrinho):
    acrescimo_total = float(input("Valor do acréscimo total: "))
    carrinho.distribuir_acrescimo_total(acrescimo_total)


def aplicar_desconto_total(carrinho):
    desconto_total = float(input("Valor do desconto total: "))
    carrinho.distribuir_desconto_total(desconto_total)


def listar_itens_disponiveis(itens_disponiveis):
    print("\nItens disponíveis:")
    for item in itens_disponiveis:
        print(f"{item['descricao']} (Código: {item['codigo']}, Valor: {item['valor']})")
