def main():
    """
    Função principal que simula um jogo de pôquer simplificado
    e determina o vencedor com base na pontuação total.
    """
    print("--- Jogo de Pôquer Simplificado ---")
    print("O programa irá calcular o vencedor de um torneio com base na pontuação final.")
    print("O vencedor é quem tiver a maior pontuação. Em caso de empate, o jogador com o maior índice vence.")
    
    # Valida e lê o número de jogadores
    while True:
        try:
            num_jogadores = int(input("\nDigite o número de jogadores: "))
            if num_jogadores > 0:
                break
            else:
                print("Valor inválido. Digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    # Valida e lê o número de rodadas
    while True:
        try:
            num_rodadas = int(input("Digite o número de rodadas: "))
            if num_rodadas > 0:
                break
            else:
                print("Valor inválido. Digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

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

    # Encontra o vencedor com base na maior pontuação e na regra de desempate
    vencedor_final = 0
    maior_pontuacao_encontrada = -1

    for k in range(num_jogadores):
        if pontuacao_jogadores[k] >= maior_pontuacao_encontrada:
            maior_pontuacao_encontrada = pontuacao_jogadores[k]
            vencedor_final = k + 1 

    print(f"\nPontuação final dos jogadores: {pontuacao_jogadores}")
    print(f"O vencedor do jogo é o jogador: {vencedor_final}")

if __name__ == "__main__":
    main()