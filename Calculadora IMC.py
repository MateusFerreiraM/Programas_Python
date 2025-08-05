def calcular_imc(peso, altura_m):
    """
    Calcula o IMC a partir do peso (kg) e altura (m).
    """
    return peso / altura_m ** 2

def classificar_imc(imc):
    """
    Classifica o IMC em uma categoria de saúde.
    """
    if imc < 18.5:
        return "Abaixo do peso!"
    elif imc < 25:
        return "Saudável!"
    elif imc < 30:
        return "Peso em Excesso!"
    elif imc < 35:
        return "Obesidade Grau 1!"
    elif imc < 40:
        return "Obesidade Grau 2 (severa)!"
    else:
        return "Obesidade Grau 3 (mórbida)!"

def main():
    """
    Função principal que gerencia o fluxo do programa de cálculo de IMC.
    """
    print("--- Calculadora de IMC ---")
    print("Este programa calcula seu Índice de Massa Corporal (IMC) e o classifica.")
    
    # Validação da entrada para peso
    while True:
        try:
            peso = float(input("\nDigite seu peso em Kg: "))
            if peso > 0:
                break
            else:
                print("O peso deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    # Validação da entrada para altura em centímetros
    while True:
        try:
            altura_cm = float(input("Digite sua altura em centímetros: "))
            if altura_cm > 0:
                # Converte centímetros para metros
                altura_m = altura_cm / 100
                break
            else:
                print("A altura deve ser um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Executa os cálculos e a classificação
    imc_calculado = calcular_imc(peso, altura_m)
    classificacao = classificar_imc(imc_calculado)
    
    # Imprime os resultados
    print(f"\nSeu IMC é: {imc_calculado:.4f}")
    print(classificacao)

if __name__ == "__main__":
    main()