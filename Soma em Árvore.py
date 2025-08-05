def main():
    """
    Função principal que reduz uma lista somando pares de elementos adjacentes.
    """
    print("--- Redutor de Soma de Lista ---")
    
    # Lê e valida a lista de entrada
    while True:
        try:
            lista_original = [int(x) for x in input("Digite os valores da lista (separados por espaço): ").split()]
            if not lista_original:
                print("A lista não pode estar vazia.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    # Inicia o processo de redução
    lista_atual = lista_original[:] # Cria uma cópia da lista original
    print(f"\nLista inicial: {lista_atual}")

    # O loop continua enquanto houver mais de um elemento na lista
    while len(lista_atual) > 1:
        nova_lista = []
        
        # Percorre a lista atual em passos de 2 para somar os pares
        for i in range(0, len(lista_atual) - 1, 2):
            soma = lista_atual[i] + lista_atual[i+1]
            nova_lista.append(soma)
            
        # Lida com o caso de lista com número ímpar de elementos
        if len(lista_atual) % 2 != 0:
            nova_lista.append(lista_atual[-1])
            
        lista_atual = nova_lista
        print(f"Próxima etapa: {lista_atual}")

    print(f"\nO resultado final é: {lista_atual[0] if lista_atual else None}")

if __name__ == "__main__":
    main()