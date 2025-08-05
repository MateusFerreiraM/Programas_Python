def main():
    """
    Função principal para calcular o crescimento de um investimento.
    """
    print("--- Calculadora de Juros Compostos ---")
    
    # Leitura e validação do investimento mensal
    while True:
        try:
            investimento_mensal = float(input("Digite o valor do investimento mensal: "))
            if investimento_mensal >= 0:
                break
            print("O valor do investimento deve ser não negativo.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Leitura e validação da taxa de juros
    while True:
        try:
            taxa_juros = float(input("Digite a taxa de juros mensal (Ex: 1.5 para 1.5%): "))
            if taxa_juros >= 0:
                break
            print("A taxa de juros deve ser não negativa.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    total_acumulado = 0.0
    ano = 1
    
    continuar = "S"
    while continuar.upper() == "S":
        for i in range(1, 13):
            # Adiciona o investimento do mês
            total_acumulado += investimento_mensal
            # Aplica os juros compostos
            total_acumulado += total_acumulado * (taxa_juros / 100)
            
        print(f"Saldo do investimento após {ano} ano(s): {total_acumulado:.2f}")
        
        continuar = input("Deseja processar mais 1 ano? (S/N): ")
        ano += 1

    print("\nPrograma encerrado.")

if __name__ == "__main__":
    main()