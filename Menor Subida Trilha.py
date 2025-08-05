def calcular_subida_total(alturas):
    """
    Calcula a subida total de uma trilha em uma direção específica.
    """
    subida = 0
    # O loop compara a altura atual com a anterior
    for i in range(1, len(alturas)):
        diferenca = alturas[i] - alturas[i-1]
        if diferenca > 0:
            subida += diferenca
    return subida

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    print("--- Encontrar a Trilha com Menor Subida ---")

    # Lê e valida o número de trilhas
    while True:
        try:
            N = int(input("\nDigite o número de trilhas para analisar: "))
            if N > 0:
                break
            else:
                print("O número de trilhas deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    trilha_menor_subida = -1
    min_subida_total = float('inf') # Inicializa com um valor infinito para garantir a primeira comparação

    for i in range(N):
        print(f"\n--- Trilha {i+1} ---")
        
        while True:
            try:
                valores = input("Digite o número de alturas e os valores (Ex: 5 100 110 105 120 115): ").split()
                # O primeiro valor é o número de alturas (M)
                M = int(valores[0])
                # Os valores de altitude começam a partir do segundo elemento
                altitudes = [int(x) for x in valores[1:]]

                # Verifica se o número de altitudes lidas é o esperado
                if len(altitudes) == M:
                    break
                else:
                    print(f"Erro: Espera-se {M} altitudes, mas foram fornecidas {len(altitudes)}.")
            except (ValueError, IndexError):
                print("Entrada inválida. Siga o formato 'M alt1 alt2 ...'.")
        
        # Calcula a subida total para o percurso de ida
        subida_ida = calcular_subida_total(altitudes)
        
        # Calcula a subida total para o percurso de volta
        altitudes_reversa = altitudes[::-1]
        subida_volta = calcular_subida_total(altitudes_reversa)
        
        # A subida total para a trilha é o mínimo entre ida e volta
        subida_atual = min(subida_ida, subida_volta)
        
        # Encontra a trilha com a menor subida total
        if subida_atual < min_subida_total:
            min_subida_total = subida_atual
            trilha_menor_subida = i + 1

    print(f"\nA trilha com a menor subida total é a {trilha_menor_subida}.")

if __name__ == "__main__":
    main()