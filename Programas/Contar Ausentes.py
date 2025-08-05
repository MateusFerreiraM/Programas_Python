def contar_ausentes(lista_itens, lista_base):
    """
    Conta quantos itens da 'lista_itens' não estão presentes na 'lista_base'.
    
    Args:
        lista_itens (list): A lista de itens a serem verificados.
        lista_base (list): A lista base onde a presença dos itens será checada.
        
    Returns:
        int: A contagem de itens ausentes.
    """
    # A principal otimização: converter a lista_base para um set.
    # A busca por um item em um set é muito mais rápida (O(1)) do que em uma lista (O(N)).
    set_base = set(lista_base)
    
    contagem = 0
    for item in lista_itens:
        if item not in set_base:
            contagem += 1
            
    return contagem

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    print("--- Contador de Itens Ausentes ---")
    print("Este programa compara duas listas e conta quantos itens da primeira")
    print("lista não estão presentes na segunda.")

    # A linha de entrada de n, c, m foi removida por não ser usada.
    
    # Lê as listas com validação de entrada
    print("\nDigite os itens da primeira lista (capas), separados por espaços:")
    capas = input().split()
    
    print("Digite os itens da segunda lista (volumes que você já tem), separados por espaços:")
    volumes = input().split()
    
    # Chama a função de contagem
    contagem_ausentes = contar_ausentes(capas, volumes)
    
    print(f"\nO número de itens ausentes é: {contagem_ausentes}")

if __name__ == "__main__":
    main()