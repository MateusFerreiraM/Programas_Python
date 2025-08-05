def main():
    """
    Função principal que cria e exibe uma matriz de zeros com dimensões
    definidas pelo usuário.
    """
    print("--- Criador de Matriz de Zeros ---")
    print("Este programa cria e exibe uma matriz com todos os valores zerados.")

    # Lê e valida as dimensões da matriz
    while True:
        try:
            l, c = map(int, input("\nDigite o número de linhas e colunas, separados por um espaço: ").split())
            if l > 0 and c > 0:
                break
            else:
                print("Os números de linhas e colunas devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    # Cria a matriz de forma concisa usando list comprehension
    matriz = [[0 for _ in range(c)] for _ in range(l)]

    # Imprime a matriz de forma formatada
    print("\nMatriz criada:")
    for linha in matriz:
        # Usa 'join' para imprimir os elementos separados por espaço
        print(" ".join(map(str, linha)))

if __name__ == "__main__":
    main()