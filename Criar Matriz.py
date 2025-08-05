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
    Função principal que cria e exibe uma matriz com valores do usuário.
    """
    print("--- Criador e Impressor de Matriz ---")

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

    matriz = ler_matriz(l, c)
    
    imprimir_matriz(matriz, "Matriz Criada")

if __name__ == "__main__":
    main()