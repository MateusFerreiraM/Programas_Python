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
    Função principal que calcula e imprime a matriz transposta.
    """
    print("--- Calculadora de Matriz Transposta ---")

    # Lê e valida as dimensões da matriz
    while True:
        try:
            l, c = map(int, input("\nDigite o número de linhas e colunas: ").split())
            if l > 0 and c > 0:
                break
            else:
                print("As dimensões devem ser números inteiros positivos.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    matriz_original = ler_matriz(l, c)
    
    # `zip(*matriz_original)` "desempacota" a matriz, transformando linhas em colunas
    matriz_transposta = [list(linha) for linha in zip(*matriz_original)]
    
    imprimir_matriz(matriz_original, "Matriz Original")
    imprimir_matriz(matriz_transposta, "Matriz Transposta")

if __name__ == "__main__":
    main()