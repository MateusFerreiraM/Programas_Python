def ler_matriz(num_linhas, num_colunas):
    """
    Lê os valores de uma matriz, com validação de entrada.
    """
    matriz = []
    print("\nPreencha a matriz:")
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

def imprimir_matriz(matriz):
    """
    Imprime a matriz de forma formatada.
    """
    for linha in matriz:
        # Formata a impressão para ter 2 casas decimais e alinhamento
        print(" ".join(f"{valor:7.2f}" for valor in linha))

def main():
    """
    Função principal que multiplica a diagonal principal de uma matriz.
    """
    print("--- Multiplicador da Diagonal Principal ---")

    # Lê e valida as dimensões da matriz
    while True:
        try:
            l, c = map(int, input("\nDigite o número de linhas e colunas (matriz quadrada): ").split())
            if l == c and l > 0:
                break
            else:
                print("Por favor, digite dois números inteiros positivos iguais (matriz quadrada).")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    matriz = ler_matriz(l, c)
    
    # Lê e valida o valor do multiplicador
    while True:
        try:
            k = float(input("Qual valor você quer multiplicar a diagonal principal: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número.")
    
    print("\nAntes da Multiplicação:")
    imprimir_matriz(matriz)

    # Multiplica a diagonal principal
    for i in range(l):
        matriz[i][i] = matriz[i][i] * k

    print("\nDepois da Multiplicação:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()