def inverter_numero(num):
    """
    Inverte um número inteiro de forma eficiente e segura.
    """
    if num < 0:
        # Lida com números negativos
        sinal = -1
        num = abs(num)
    else:
        sinal = 1
        
    invertido = 0
    while num > 0:
        ultimo_digito = num % 10
        invertido = invertido * 10 + ultimo_digito
        num = num // 10
        
    return invertido * sinal

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    print("--- Inversor de Números ---")
    print("Este programa inverte os dígitos de um número inteiro.")
    
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    numero_invertido = inverter_numero(num)

    print(f"\nNúmero Original: {num} \nNúmero Invertido: {numero_invertido}\n")

if __name__ == "__main__":
    main()