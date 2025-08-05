def ler_matriz(num_linhas, num_colunas):
    """Lê os valores de uma matriz, garantindo a quantidade correta de colunas."""
    matriz = []
    print(f"\nDigite os valores de cada linha, separados por um espaço:")
    for i in range(num_linhas):
        while True:
            try:
                linha = list(map(int, input(f"Linha {i+1}: ").split()))
                if len(linha) == num_colunas:
                    matriz.append(linha)
                    break
                else:
                    print(f"Erro: A linha deve ter exatamente {num_colunas} valores.")
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros.")
    return matriz

def main():
    """Função principal que gerencia a execução do programa."""
    print("\n--- Encontrar a Soma Máxima da Matriz ---")
    print("Este programa lê uma matriz e encontra a maior soma de uma linha ou coluna.\n")

    # Lê e valida as dimensões da matriz
    while True:
        try:
            n, m = map(int, input("Digite o número de linhas e colunas (Ex: 3 4): ").split())
            if n > 0 and m > 0:
                break
            else:
                print("Os números de linhas e colunas devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    matriz = ler_matriz(n, m)

    # --- Calcular a maior soma das linhas ---
    somas_linhas = [sum(linha) for linha in matriz]
    soma_maxima = max(somas_linhas)

    # --- Calcular a maior soma das colunas ---
    # `zip(*matriz)` inverte a matriz, transformando linhas em colunas
    somas_colunas = [sum(coluna) for coluna in zip(*matriz)]
    
    # Atualiza a soma máxima se a maior soma de coluna for maior
    soma_maxima = max(soma_maxima, max(somas_colunas))

    print(f"\nA maior soma encontrada em linhas ou colunas é: {soma_maxima}")

if __name__ == "__main__":
    main()