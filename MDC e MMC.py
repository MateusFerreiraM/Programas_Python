import math

def calcular_mdc(a, b):
    """
    Calcula o MDC de dois números usando o Algoritmo de Euclides.
    É o método mais rápido e eficiente.
    """
    # MDC(a, 0) = a
    if b == 0:
        return a
    
    # O algoritmo funciona de forma recursiva ou iterativa
    # Usamos o método iterativo com um loop while
    while b:
        a, b = b, a % b
        
    return abs(a)

def calcular_mmc(a, b):
    """
    Calcula o MMC de dois números usando a fórmula: MMC(a,b) = (a * b) / MDC(a,b).
    """
    if a == 0 or b == 0:
        return 0
    
    # A fórmula exige o MDC
    mdc = calcular_mdc(a, b)
    
    # Usa abs() para lidar com números negativos, garantindo um MMC positivo
    return abs(a * b) // mdc

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Calculadora de MDC e MMC ---")
    print("Este programa calcula o Máximo Divisor Comum e o Mínimo Múltiplo Comum.")
    
    while True:
        try:
            a, b = map(int, input("\nDigite dois números inteiros, separados por espaço: ").split())
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    # A validação de a e b como 0 é feita dentro das funções, evitando erros
    mdc_result = calcular_mdc(a, b)
    mmc_result = calcular_mmc(a, b)

    print(f"\nO Máximo Divisor Comum (MDC) de {a} e {b} é: {mdc_result}")
    print(f"O Mínimo Múltiplo Comum (MMC) de {a} e {b} é: {mmc_result}")

if __name__ == "__main__":
    main()