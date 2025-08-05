def remover_duplicatas(lista):
    """
    Remove duplicatas de uma lista de forma eficiente.
    """
    return list(set(lista))

def intercalar_listas(lista1, lista2):
    """
    Intercala os elementos de duas listas, independentemente de seus tamanhos.
    """
    lista_intercalada = []
    tamanho_menor = min(len(lista1), len(lista2))
    
    # Intercala até o final da menor lista
    for i in range(tamanho_menor):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
        
    # Adiciona os elementos restantes da lista maior
    if len(lista1) > len(lista2):
        lista_intercalada.extend(lista1[tamanho_menor:])
    else:
        lista_intercalada.extend(lista2[tamanho_menor:])
        
    return lista_intercalada

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Processador de Listas ---")
    print("Este programa intercala duas listas, remove duplicatas e imprime o resultado.")

    # Valida e lê a lista 1
    while True:
        try:
            input_str1 = input("Preencha a lista 1 (números separados por espaço): ")
            lista1 = [int(x) for x in input_str1.split()]
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    # Valida e lê a lista 2
    while True:
        try:
            input_str2 = input("Preencha a lista 2 (números separados por espaço): ")
            lista2 = [int(x) for x in input_str2.split()]
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    # Intercala as listas
    lista_final = intercalar_listas(lista1, lista2)
    
    # Remove as duplicatas
    lista_final_sem_duplicatas = remover_duplicatas(lista_final)
    lista_final_sem_duplicatas.sort()
    
    print(f"\nLista final (sem duplicatas e ordenada): {lista_final_sem_duplicatas}")

if __name__ == "__main__":
    main()