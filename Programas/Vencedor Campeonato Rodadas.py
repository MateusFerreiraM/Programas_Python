def main():
    """
    Função principal que calcula a pontuação total de jogadores
    e determina o vencedor em um campeonato.
    """
    print("--- Vencedor do Campeonato ---")
    
    # Valida e lê o número de jogadores e rodadas
    while True:
        try:
            num_jogadores, num_rodadas = map(int, input("\nDigite o número de jogadores e de rodadas: ").split())
            if num_jogadores > 0 and num_rodadas > 0:
                break
            else:
                print("Valores inválidos. Digite números inteiros positivos.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    # Inicializa a pontuação de cada jogador
    pontuacao_jogadores = [0] * num_jogadores

    # Loop para ler os placares de cada rodada separadamente
    for i in range(num_rodadas):
        while True:
            try:
                placar_rodada = list(map(int, input(f"Digite os placares da Rodada {i+1} ({num_jogadores} placares): ").split()))
                if len(placar_rodada) == num_jogadores:
                    # Adiciona os placares da rodada à pontuação total de cada jogador
                    for k in range(num_jogadores):
                        pontuacao_jogadores[k] += placar_rodada[k]
                    break
                else:
                    print(f"Erro: Forneça exatamente {num_jogadores} placares para esta rodada.")
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros.")

    # Encontra o vencedor com base na maior pontuação e na regra de desempate (maior índice)
    vencedor = 0
    max_pontuacao = -1

    for k in range(num_jogadores):
        if pontuacao_jogadores[k] >= max_pontuacao:
            max_pontuacao = pontuacao_jogadores[k]
            vencedor = k + 1 # o índice do jogador é 1-based

    print(f"\nPontuação final dos jogadores: {pontuacao_jogadores}")
    print(f"O vencedor é o jogador: {vencedor}")

if __name__ == "__main__":
    main()