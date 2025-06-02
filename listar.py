from estoque import estoque

def listar_produtos():
    """
    Lista todos os produtos disponíveis no estoque.
    """
    if not estoque:
        print("⚠️ Estoque vazio.")
    else:
        print("📦 Produtos no Estoque:")
        print("-" * 40)
        for produto in estoque:
            print(f"Código: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("-" * 40)
