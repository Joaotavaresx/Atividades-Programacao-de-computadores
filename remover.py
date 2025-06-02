def remover_produto():
    visualizar_estoque()
    produto = input("Nome do produto a remover: ")
    if produto in estoque:
        quantidade = int(input("Quantidade a remover: "))
        if quantidade >= estoque[produto]:
            del estoque[produto]
            print(f"{produto} removido do estoque.\n")
        else:
            estoque[produto] -= quantidade
            print(f"{quantidade} unidades de {produto} removidas.\n")
        salvar_estoque()
    else:
        print("Produto não encontrado no estoque.\n")
