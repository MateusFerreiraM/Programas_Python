import math

def fatorial(num):
    """
    Calcula o fatorial de um número inteiro não negativo.
    """
    if num <= 1:
        return 1
    
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
        
    return resultado

def calcular_combinacao(n, m):
    """
    Calcula o número de combinações de 'n' elementos, tomados 'm' a 'm'.
    """
    if m < 0 or m > n:
        return 0
        
    fatorial_n = fatorial(n)
    fatorial_m = fatorial(m)
    fatorial_nm = fatorial(n - m)
    
    combinacoes = fatorial_n / (fatorial_m * fatorial_nm)
    return combinacoes

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Calculadora de Combinações (n escolhe m) ---")
    print("Este programa calcula o número de combinações possíveis.")
    
    # Explicação para o usuário
    print("\nOnde 'n' é o número TOTAL de itens, e 'm' é o número de itens a serem ESCOLHIDOS.")
    print("Exemplo: De 5 frutas, quantas combinações de 3 frutas eu posso escolher?")
    
    while True:
        try:
            n, m = map(int, input("\nDigite n (total de itens) e m (itens a escolher), separados por um espaço: ").split())
            if n >= 0 and m >= 0 and n >= m:
                break
            else:
                print("Entrada inválida. 'n' e 'm' devem ser não negativos, e 'n' deve ser maior ou igual a 'm'.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    combinacao = calcular_combinacao(n, m)
    
    print(f"\nO número de combinações de {n} elementos tomados {m} a {m} é: {int(combinacao)}")
    
if __name__ == "__main__":
    main()