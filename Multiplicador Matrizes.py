def ler_matriz(titulo, num_linhas, num_colunas):
    """
    Lê os valores de uma matriz, com validação de entrada.
    """
    matriz = []
    print(f"\nPreencha a {titulo}:")
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            while True:
                try:
                    valor = float(input(f"Valor da posição ({i+1}, {j+1}): "))
                    linha.append(valor)
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número.")
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz, titulo=""):
    """
    Imprime a matriz de forma formatada.
    """
    if titulo:
        print(f"\n{titulo}:")
    for linha in matriz:
        print(" ".join(f"{valor:7.2f}" for valor in linha))

def main():
    """
    Função principal que multiplica duas matrizes.
    """
    print("--- Multiplicador de Matrizes ---")
    print("Para multiplicar A x B, o número de colunas de A deve ser igual ao número de linhas de B.")
    
    # Lê e valida as dimensões da Matriz A
    while True:
        try:
            l_a, c_a = map(int, input("\nDigite o número de linhas e colunas da Matriz A: ").split())
            if l_a > 0 and c_a > 0:
                break
            print("As dimensões devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")
            
    # Lê e valida as dimensões da Matriz B
    while True:
        try:
            l_b, c_b = map(int, input("Digite o número de linhas e colunas da Matriz B: ").split())
            if l_b > 0 and c_b > 0:
                break
            print("As dimensões devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    # Verifica a condição de multiplicação
    if c_a != l_b:
        print("\nEssas matrizes não podem ser multiplicadas!")
        print(f"O número de colunas da Matriz A ({c_a}) deve ser igual ao número de linhas da Matriz B ({l_b}).")
        return

    matriz_a = ler_matriz("Matriz A", l_a, c_a)
    matriz_b = ler_matriz("Matriz B", l_b, c_b)
    
    imprimir_matriz(matriz_a, "Matriz A (Original)")
    imprimir_matriz(matriz_b, "Matriz B (Original)")

    # Realiza a multiplicação de matrizes
    matriz_resultante = []
    for linha in range(l_a):
        matriz_resultante.append([])
        for coluna in range(c_b):
            soma_produto = 0
            for k in range(c_a):
                soma_produto += matriz_a[linha][k] * matriz_b[k][coluna]
            matriz_resultante[linha].append(soma_produto)

    imprimir_matriz(matriz_resultante, "Matriz Multiplicada")

if __name__ == "__main__":
    main()