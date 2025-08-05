def encontrar_maior_sequencia(cartas):
    """
    Encontra e retorna o tamanho da maior sequência de cartas idênticas.
    
    Args:
        cartas (list): Uma lista de strings representando as cartas.
    
    Returns:
        int: O tamanho da maior sequência. Retorna 0 para uma lista vazia.
    """
    if not cartas:
        return 0

    maior_sequencia = 1
    contagem_atual = 1

    # Percorre a lista até o penúltimo elemento
    for i in range(len(cartas) - 1):
        if cartas[i] == cartas[i+1]:
            contagem_atual += 1
        else:
            # A sequência foi quebrada. Atualiza a maior sequência encontrada
            maior_sequencia = max(maior_sequencia, contagem_atual)
            # Reinicia a contagem para 1 para a nova carta
            contagem_atual = 1
    
    # IMPORTANTE: Verifica a última sequência após o loop, pois ela pode ser a maior
    maior_sequencia = max(maior_sequencia, contagem_atual)
    
    return maior_sequencia

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("\n--- Encontrar Maior Sequência de Cartas ---")
    print("Este programa encontra a maior sequência de cartas idênticas em uma linha.")
    
    # --- Entrada do número de cartas ---
    while True:
        try:
            n = int(input("Digite o número total de cartas: "))
            if n > 0:
                break
            print("O número de cartas deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # --- Entrada das cartas ---
    while True:
        cartas = input(f"Digite as {n} cartas separadas por espaços: ").split()
        if len(cartas) == n:
            break
        print(f"Erro: Você digitou {len(cartas)} cartas, mas o esperado era {n}.")
    
    resultado = encontrar_maior_sequencia(cartas)
    print(f"\nA maior sequência de cartas idênticas é: {resultado}")


if __name__ == "__main__":
    main()