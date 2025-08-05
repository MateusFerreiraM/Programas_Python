def calcular_lucro_maximo_intuitivo(precos_bolsa, taxa):
    """
    Calcula o lucro máximo a partir de preços de ações, simulando
    transações de compra e venda de forma intuitiva.
    """
    if not precos_bolsa:
        return 0

    lucro_total = 0
    preco_compra = precos_bolsa[0]

    for preco_atual in precos_bolsa[1:]:
        # Se o preço atual for mais baixo que o nosso preço de compra,
        # é uma oportunidade melhor para comprar.
        if preco_atual < preco_compra:
            preco_compra = preco_atual
        
        # Se o preço subiu o suficiente para cobrir a taxa,
        # simulamos uma venda.
        elif preco_atual - preco_compra > taxa:
            lucro = preco_atual - preco_compra - taxa
            lucro_total += lucro
            
            # Após a venda, reiniciamos a procura por um novo preço de compra,
            # usando o preço atual como base.
            preco_compra = preco_atual

    return lucro_total


def main():
    """
    Função principal que gerencia a entrada, cálculo e saída do programa.
    """
    print("\n--- Calculadora de Lucro Máximo da Bolsa (Simulação) ---")
    print("Este programa calcula o lucro máximo que você pode obter comprando e vendendo ações.")
    print("Ele simula uma estratégia onde você compra a um preço baixo e vende a um preço alto,")
    print("sempre considerando uma taxa de transação a cada lucro.")

    while True:
        try:
            entrada = input("\nDigite o número de dias e a taxa de transação, separados por um espaço: ")
            dias, taxa = map(int, entrada.split())
            if dias <= 0 or taxa < 0:
                print("O número de dias deve ser maior que zero e a taxa não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite dois números inteiros.")

    while True:
        try:
            print(f"Digite os preços das ações para os {dias} dias, separados por um espaço:")
            precos = list(map(int, input().split()))
            if len(precos) != dias:
                print(f"Número incorreto de preços. Por favor, digite exatamente {dias} preços.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    lucro_final = calcular_lucro_maximo_intuitivo(precos, taxa)
    
    print(f"\nO lucro máximo possível, seguindo a estratégia, é: {lucro_final}")

if __name__ == "__main__":
    main()