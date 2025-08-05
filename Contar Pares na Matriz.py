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
                    valor = int(input(f"Valor da posição ({i+1}, {j+1}): "))
                    linha.append(valor)
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz, titulo=""):
    """
    Imprime a matriz de forma formatada.
    """
    if titulo:
        print(f"\n{titulo}:")
    for linha in matriz:
        print(" ".join(f"{valor:3d}" for valor in linha))

def main():
    """
    Função principal que conta os números pares em uma matriz.
    """
    print("--- Contador de Pares em Matriz ---")

    # Lê e valida as dimensões da matriz
    while True:
        try:
            l, c = map(int, input("\nDigite o número de linhas e colunas, separados por espaço: ").split())
            if l > 0 and c > 0:
                break
            else:
                print("As dimensões devem ser números inteiros positivos.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    matriz = ler_matriz(l, c)
    
    # Conta os números pares de forma concisa usando list comprehension
    pares = sum(1 for linha in matriz for valor in linha if valor % 2 == 0)

    imprimir_matriz(matriz, "Matriz")
    
    print(f"\nA matriz possui {pares} números pares.")

if __name__ == "__main__":
    main()