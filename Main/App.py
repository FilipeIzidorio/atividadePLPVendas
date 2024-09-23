# Função para inicializar itens predefinidos
def inicializar_itens_predefinidos():
    return [
        {"codigo": "001", "descricao": "Mouse", "valor": 50.0, "acrescimo": 0, "desconto": 0},
        {"codigo": "002", "descricao": "Teclado", "valor": 100.0, "acrescimo": 0, "desconto": 0},
        {"codigo": "003", "descricao": "Monitor", "valor": 750.0, "acrescimo": 0, "desconto": 0},
        {"codigo": "004", "descricao": "Cadeira Gamer", "valor": 500.0, "acrescimo": 0, "desconto": 0},
        {"codigo": "005", "descricao": "Fone de Ouvido", "valor": 150.0, "acrescimo": 0, "desconto": 0},
        {"codigo": "006", "descricao": "Notebook", "valor": 3000.0, "acrescimo": 0, "desconto": 0},
        {"codigo": "007", "descricao": "Impressora", "valor": 200.0, "acrescimo": 0, "desconto": 0}
    ]


# Função para exibir o menu
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


# Função para listar os itens disponíveis
def listar_itens_disponiveis(itens_disponiveis):
    print("\nItens disponíveis:")
    for item in itens_disponiveis:
        print(f"{item['descricao']} (Código: {item['codigo']}, Valor: {item['valor']:.2f})")


# Função para inserir item no carrinho
def inserir_item(carrinho, itens_disponiveis):
    listar_itens_disponiveis(itens_disponiveis)
    escolha = int(input("\nEscolha o número do item para adicionar ao carrinho: ")) - 1

    if 0 <= escolha < len(itens_disponiveis):
        item_escolhido = itens_disponiveis[escolha].copy()  # Copia o item para o carrinho
        carrinho.append(item_escolhido)
        print(f"\nItem '{item_escolhido['descricao']}' adicionado ao carrinho.")
    else:
        print("Opção inválida!")


# Função para aplicar acréscimo em um item do carrinho
def aplicar_acrescimo_item(carrinho):
    codigo = input("Código do item: ")
    acrescimo = float(input("Valor do acréscimo: "))

    for item in carrinho:
        if item['codigo'] == codigo:
            item['acrescimo'] += acrescimo
            item['valor'] += acrescimo
            print(f"Acréscimo de {acrescimo:.2f} aplicado ao item {item['descricao']}.")
            return
    print("Item não encontrado.")


# Função para aplicar desconto em um item do carrinho
def aplicar_desconto_item(carrinho):
    codigo = input("Código do item: ")
    desconto = float(input("Valor do desconto: "))

    for item in carrinho:
        if item['codigo'] == codigo:
            item['desconto'] += desconto
            item['valor'] -= desconto
            print(f"Desconto de {desconto:.2f} aplicado ao item {item['descricao']}.")
            return
    print("Item não encontrado.")


# Função para aplicar acréscimo total distribuído no carrinho
def aplicar_acrescimo_total(carrinho):
    acrescimo_total = float(input("Valor do acréscimo total: "))

    if len(carrinho) == 0:
        print("O carrinho está vazio.")
        return

    acrescimo_por_item = acrescimo_total / len(carrinho)
    for item in carrinho:
        item['acrescimo'] += acrescimo_por_item
        item['valor'] += acrescimo_por_item
    print(f"Acréscimo total de {acrescimo_total:.2f} distribuído igualmente entre os itens.")


# Função para aplicar desconto total distribuído no carrinho
def aplicar_desconto_total(carrinho):
    desconto_total = float(input("Valor do desconto total: "))

    if len(carrinho) == 0:
        print("O carrinho está vazio.")
        return

    desconto_por_item = desconto_total / len(carrinho)
    for item in carrinho:
        item['desconto'] += desconto_por_item
        item['valor'] -= desconto_por_item
    print(f"Desconto total de {desconto_total:.2f} distribuído igualmente entre os itens.")


# Função para listar os itens no carrinho
def listar_itens_carrinho(carrinho):
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        print("\nItens no carrinho:")
        for item in carrinho:
            print(f"Código: {item['codigo']}, Descrição: {item['descricao']}, Valor: {item['valor']:.2f}, "
                  f"Acréscimo: {item['acrescimo']:.2f}, Desconto: {item['desconto']:.2f}")


# Função para finalizar a venda e mostrar o resumo
def finalizar_venda(carrinho):
    total_acrescimo = sum(item['acrescimo'] for item in carrinho)
    total_desconto = sum(item['desconto'] for item in carrinho)
    valor_final = sum(item['valor'] for item in carrinho)

    print("\nResumo da venda:")
    listar_itens_carrinho(carrinho)
    print(f"\nAcréscimo total: {total_acrescimo:.2f}")
    print(f"Desconto total: {total_desconto:.2f}")
    print(f"Valor final: {valor_final:.2f}")


# Função principal para executar o sistema
def main():
    carrinho = []
    itens_disponiveis = inicializar_itens_predefinidos()

    while True:
        exibir_menu()
        opcao = int(input())

        if opcao == 1:
            inserir_item(carrinho, itens_disponiveis)
        elif opcao == 2:
            aplicar_acrescimo_item(carrinho)
        elif opcao == 3:
            aplicar_desconto_item(carrinho)
        elif opcao == 4:
            aplicar_acrescimo_total(carrinho)
        elif opcao == 5:
            aplicar_desconto_total(carrinho)
        elif opcao == 6:
            listar_itens_carrinho(carrinho)
        elif opcao == 7:
            listar_itens_disponiveis(itens_disponiveis)
        elif opcao == 8:
            finalizar_venda(carrinho)
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
