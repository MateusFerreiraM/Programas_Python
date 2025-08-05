def gerar_fibonacci(n):
    """
    Gera uma lista com os 'n+1' primeiros números da sequência de Fibonacci.
    
    Args:
        n (int): O índice do último termo a ser gerado (f_n).
        
    Returns:
        list: Uma lista com os números da sequência.
    """
    if n < 0:
        return []
    if n == 0:
        return [0]
    
    fib_list = [0, 1]
    
    # O loop vai de 2 até n, gerando os termos subsequentes
    for _ in range(2, n + 1):
        proximo_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(proximo_fib)
        
    return fib_list

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Gerador da Sequência de Fibonacci ---")
    
    while True:
        try:
            n = int(input("Digite um número inteiro (o índice do último termo a ser exibido): "))
            if n >= 0:
                break
            else:
                print("Por favor, digite um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
    
    sequencia = gerar_fibonacci(n)
    
    # Converte a lista de números para uma string formatada para impressão
    sequencia_str = ", ".join(map(str, sequencia))
    
    print(sequencia_str)

if __name__ == "__main__":
    main()