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
        print(" ".join(f"{valor:6.2f}" for valor in linha))

def main():
    """
    Função principal que encontra a linha com a maior soma em uma matriz.
    """
    print("--- Encontrar a Linha com a Maior Soma ---")

    # Lê e valida as dimensões da matriz
    while True:
        try:
            l, c = map(int, input("Digite o número de linhas e colunas, separados por espaço: ").split())
            if l > 0 and c > 0:
                break
            else:
                print("As dimensões devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    matriz = ler_matriz(l, c)
    
    # Encontra a linha com a maior soma
    indice_maior = 0
    soma_maxima = sum(matriz[0])

    for i in range(1, l):
        soma_atual = sum(matriz[i])
        if soma_atual > soma_maxima:
            soma_maxima = soma_atual
            indice_maior = i

    print("\nMatriz preenchida:")
    imprimir_matriz(matriz)
    
    print(f"\nLinha de maior soma: {indice_maior + 1}")
    print(f"Soma: {soma_maxima:.2f}")

if __name__ == "__main__":
    main()