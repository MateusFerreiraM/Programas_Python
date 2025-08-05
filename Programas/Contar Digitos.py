def contar_digitos(numero):
    """
    Conta o número de dígitos em um número inteiro, ignorando o sinal.
    Ex: -123 terá 3 dígitos.
    """
    # Usa a função abs() para tratar números negativos
    return len(str(abs(numero)))

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Contador de Dígitos ---")
    print("Este programa conta quantos dígitos um número inteiro possui.")
    
    while True:
        try:
            num = int(input('Forneça um número inteiro: '))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    dig = contar_digitos(num)
    
    # Usa uma f-string para uma saída mais limpa
    print(f"O número {num} possui {dig} dígito(s)!")

if __name__ == "__main__":
    main()