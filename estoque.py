estoque = []

def adicionar_produto():
    """
    Função que adiciona um novo produto ao estoque.
    Verifica se o código já existe para evitar duplicidade.
    """
    codigo = input("Código do produto: ")
    for produto in estoque:
        if produto['codigo'] == codigo:
            print("Produto já cadastrado.")
            return
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço unitário: "))

    novo_produto = {
        'codigo': codigo,
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }

    estoque.append(novo_produto)
    print("✅ Produto adicionado com sucesso.")