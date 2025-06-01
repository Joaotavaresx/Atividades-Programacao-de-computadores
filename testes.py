from estoque import estoque
from remover import remover_produto
from listar import listar_produtos

def teste_simples():
    print("\n--- Teste 1: Adicionar Produto ---")
    estoque.append({'codigo': '001', 'nome': 'Caneta', 'quantidade': 10, 'preco': 1.50})
    listar_produtos()

    print("\n--- Teste 2: Remover Produto ---")
    remover_produto()

    print("\n--- Teste 3: Listar Estoque Vazio ---")
    listar_produtos()

if __name__ == "__main__":
    teste_simples()