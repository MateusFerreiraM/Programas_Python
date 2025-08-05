def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    print("--- Transformador de Sequência ---")
    print("Este programa verifica se uma lista pode ser transformada em uma sequência")
    print("de inteiros consecutivos e calcula o número mínimo de movimentos.")
    
    # Validação e entrada do número de elementos
    while True:
        try:
            n = int(input("\nDigite o número de elementos na lista: "))
            if n > 0:
                break
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    # Validação e entrada da lista
    while True:
        try:
            c = list(map(int, input(f"Digite os {n} números da lista, separados por espaços: ").split()))
            if len(c) == n:
                break
            else:
                print(f"Erro: Forneça exatamente {n} números.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # Calcula a soma de uma progressão aritmética de 1 a n
    soma_pa = (n * (n + 1)) // 2
    
    soma_c = sum(c)
    
    # A soma dos números da lista 'c' menos a soma da PA é a "soma inicial" da PA que buscamos.
    soma_inicial_pa = soma_c - soma_pa

    # A condição para que a transformação seja possível é que a "soma inicial"
    # seja um múltiplo de n e não seja negativa.
    if soma_inicial_pa >= 0 and soma_inicial_pa % n == 0:
        movimentos = 0
        
        # A altura inicial é o primeiro termo da PA.
        altura = (soma_inicial_pa // n) + 1
        
        # O número de movimentos é a soma das diferenças dos elementos que
        # são maiores que os elementos correspondentes na PA.
        for numero in c:
            if numero > altura:
                movimentos += numero - altura
            altura += 1
            
        print(f"\nÉ possível. O número mínimo de movimentos é: {movimentos}")
    else:
        print("\nNão é possível transformar a lista na sequência desejada.")

if __name__ == "__main__":
    main()