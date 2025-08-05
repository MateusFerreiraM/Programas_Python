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
        # Formata a impressão para ter 2 casas decimais e alinhamento
        print(" ".join(f"{valor:7.2f}" for valor in linha))

def main():
    """
    Função principal que soma duas matrizes.
    """
    print("--- Calculadora de Soma de Matrizes ---")

    # Lê e valida as dimensões das matrizes
    while True:
        try:
            l, c = map(int, input("\nDigite o número de linhas e colunas das matrizes: ").split())
            if l > 0 and c > 0:
                break
            else:
                print("As dimensões devem ser números inteiros positivos.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    # A soma de matrizes requer que as dimensões sejam as mesmas
    matriz_a = ler_matriz("Matriz A", l, c)
    matriz_b = ler_matriz("Matriz B", l, c)
    
    # Prepara a matriz resultante com zeros
    matriz_c = [[0 for _ in range(c)] for _ in range(l)]
    
    # Realiza a soma de matrizes
    for linha in range(l):
        for coluna in range(c):
            matriz_c[linha][coluna] = matriz_a[linha][coluna] + matriz_b[linha][coluna]

    # Imprime o resultado de forma visualmente clara
    imprimir_matriz(matriz_a, "Matriz A")
    print("\n+")
    imprimir_matriz(matriz_b, "Matriz B")
    print("\n=")
    imprimir_matriz(matriz_c, "Matriz C")

if __name__ == "__main__":
    main()