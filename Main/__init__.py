from Carrinho import *
def main():
    carrinho = Carrinho()
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
            carrinho.listar_itens()
        elif opcao == 7:
            listar_itens_disponiveis(itens_disponiveis)
        elif opcao == 8:
            carrinho.finalizar_venda()
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()