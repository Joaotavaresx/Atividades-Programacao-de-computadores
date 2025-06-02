from estoque import estoque

def remover_produto():
    """
    Remove um produto do estoque com base no código informado.
    """
    codigo = input("Digite o código do produto a ser removido: ")
    for produto in estoque:
        if produto['codigo'] == codigo:
            estoque.remove(produto)
            print("✅ Produto removido com sucesso.")
            return
    print("❌ Produto não encontrado.")
