def encontrar_tempo_minimo_minutos(tempos_ciclo, num_alvo):
    """
    Encontra o tempo mínimo em minutos para produzir um número alvo de itens.
    """
    limite_inferior = 1
    limite_superior = num_alvo * max(tempos_ciclo)

    tempo_minimo_encontrado = limite_superior

    while limite_inferior <= limite_superior:
        tempo_teste = (limite_inferior + limite_superior) // 2
        total_produzido = 0
        
        for tempo_ciclo in tempos_ciclo:
            total_produzido += tempo_teste // tempo_ciclo
        
        if total_produzido >= num_alvo:
            tempo_minimo_encontrado = tempo_teste
            limite_superior = tempo_teste - 1
        else:
            limite_inferior = tempo_teste + 1

    return tempo_minimo_encontrado

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("\n--- Calculadora de Tempo de Produção Mínimo ---")
    print("Este programa calcula o menor tempo em minutos para um conjunto de máquinas produzir um número de itens.")

    while True:
        try:
            num_maquinas, num_alvo = map(int, input("\nDigite o número de máquinas e o número de itens alvo: ").split())
            if num_maquinas > 0 and num_alvo > 0:
                break
            print("Entrada inválida. Os valores devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite dois números inteiros.")

    while True:
        try:
            print(f"\nDigite os tempos de ciclo de cada uma das {num_maquinas} máquinas (em minutos), separados por um espaço:")
            tempos_ciclo = list(map(int, input().split()))
            if len(tempos_ciclo) == num_maquinas and all(t > 0 for t in tempos_ciclo):
                break
            print("Entrada inválida. Certifique-se de que o número de tempos e seus valores são corretos.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    tempo_final = encontrar_tempo_minimo_minutos(tempos_ciclo, num_alvo)
    print(f"\nO tempo mínimo necessário para produzir {num_alvo} itens é: {tempo_final} minutos.")

if __name__ == "__main__":
    main()