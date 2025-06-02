estoque = []

def adicionar_produto():
    """
    Função que adiciona um novo produto ao estoque.
    Verifica se o código já existe para evitar duplicidade.
    """
    codigo = input("Código do produto: ")

    # Verifica se produto já existe
    for produto in estoque:
        if produto['codigo'] == codigo:
            print("Produto já cadastrado.")
            return   # Sai da função se produto existir
            
    # Coleta demais informações dos produtos
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço unitário: "))

    # Cria dicionário representando o novo produto
    novo_produto = {
        'codigo': codigo,
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }

    # Adiciona produto ao estoque e confirma
    estoque.append(novo_produto)
    print("✅ Produto adicionado com sucesso.")
