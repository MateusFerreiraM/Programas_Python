import math

def encontrar_divisores(n):
    """
    Encontra todos os divisores de um número n, com uma busca eficiente.
    """
    divisores = []
    # A verificação pode ir apenas até a raiz quadrada de n
    limite = int(math.sqrt(n))
    
    for i in range(1, limite + 1):
        if n % i == 0:
            divisores.append(i)
            # Se i não for a raiz quadrada de n, então (n/i) também é um divisor
            if i != n // i:
                divisores.append(n // i)
    
    divisores.sort()
    return divisores

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Verificador de Números Primos ---")
    print("Este programa encontra os divisores de um número e verifica se ele é primo.")
    
    resp = 1
    while resp == 1:
        try:
            n = int(input("\nDigite um número inteiro positivo: "))
            if n <= 0:
                print("Por favor, digite um número inteiro positivo.")
                continue

            divisores = encontrar_divisores(n)
            
            # Imprime os divisores
            print(f"Divisores de {n}: {' '.join(map(str, divisores))}")
            
            # Verifica se o número é primo
            if len(divisores) == 2:
                print(f"{n} é um número primo.")
            else:
                print(f"{n} não é um número primo.")
            
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            
        print("\nDeseja analisar outro número?")
        try:
            resp = int(input("1 = Sim | 0 = Não: "))
        except ValueError:
            print("Entrada inválida. Encerrando o programa.")
            resp = 0

if __name__ == "__main__":
    main()