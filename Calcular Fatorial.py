def calcular_fatorial(num):
    """
    Calcula o fatorial de um número inteiro não negativo.
    """
    # A base do fatorial para 0 e 1 é 1.
    if num == 0 or num == 1:
        return 1
    
    # O loop calcula o fatorial
    fatorial_calculado = 1
    while num > 1:
        fatorial_calculado *= num
        num -= 1
        
    return fatorial_calculado

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    print("--- Calculadora de Fatorial ---")
    
    # Lê e valida a entrada do usuário
    while True:
        try:
            n = int(input("Digite um valor inteiro não negativo: "))
            if n >= 0:
                break
            else:
                print("Erro. Digite um valor não negativo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    resultado = calcular_fatorial(n)
    
    print(f"O fatorial de {n} é {resultado}.")

if __name__ == "__main__":
    main()