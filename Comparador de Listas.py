def comparar_listas_de_strings(lista1, lista2):
    """
    Compara duas listas de strings e imprime as diferenças.
    Também informa se os tamanhos das listas são diferentes.
    """
    diferencas_encontradas = False
    
    # Compara as listas até o tamanho da menor
    tamanho_menor = min(len(lista1), len(lista2))
    
    for i in range(tamanho_menor):
        if lista1[i] != lista2[i]:
            print(f"Diferença na posição {i+1}: '{lista1[i]}' vs. '{lista2[i]}'")
            diferencas_encontradas = True

    # Se os tamanhos forem diferentes, isso também é uma diferença
    if len(lista1) != len(lista2):
        print(f"\nAs listas têm tamanhos diferentes.")
        print(f"Lista 1: {len(lista1)} palavras. \nLista 2: {len(lista2)} palavras.")
        diferencas_encontradas = True
    
    # Se nenhuma diferença foi encontrada
    if not diferencas_encontradas:
        print("As listas de palavras são idênticas.")

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Comparador de Listas de Palavras ---")
    print("Este programa compara duas linhas de texto palavra por palavra e destaca as diferenças.")
    
    # Lê as duas listas de palavras
    print("\nDigite a primeira linha de palavras, separadas por espaços:")
    lista1 = input().split()
    
    print("\nDigite a segunda linha de palavras, separadas por espaços:")
    lista2 = input().split()
    
    print("\n--- Resultado da Comparação ---")
    comparar_listas_de_strings(lista1, lista2)

if __name__ == "__main__":
    main()