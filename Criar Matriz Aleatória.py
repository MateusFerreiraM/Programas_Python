import random

def imprimir_matriz(matriz):
    """
    Imprime a matriz de forma formatada.
    """
    for linha in matriz:
        # Formata a impressão para ter 1 casa decimal e alinhamento
        print(" ".join(f"{valor:5.1f}" for valor in linha))

def main():
    """
    Função principal que cria e exibe uma matriz com base em regras.
    """
    print("--- Criador de Matriz com Regras ---")
    print("A matriz será preenchida com valores baseados nas suas dimensões:")
    print(" - Quadrada: com o valor da linha.")
    print(" - Larga: com números aleatórios entre 5.0 e 9.9.")
    print(" - Alta: com números aleatórios entre -10.0 e -5.0.")

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

    matriz = []

    if l == c:
        # Cria uma matriz quadrada preenchida com o valor de l
        matriz = [[l for _ in range(c)] for _ in range(l)]
    elif l < c:
        # Cria uma matriz larga com valores aleatórios positivos
        matriz = [[round(random.uniform(5, 9.9), 1) for _ in range(c)] for _ in range(l)]
    else:  # l > c
        # Cria uma matriz alta com valores aleatórios negativos
        matriz = [[round(random.uniform(-10, -5), 1) for _ in range(c)] for _ in range(l)]

    print("\nMatriz criada:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()