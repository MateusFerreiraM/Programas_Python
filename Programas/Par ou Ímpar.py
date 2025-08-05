def processar_teste(num_teste):
    """
    Processa um único caso de teste do jogo.
    """
    print(f"\n--- Teste {num_teste} ---")
    
    while True:
        try:
            rodadas = int(input("Digite o número de rodadas (0 para sair): "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    if rodadas == 0:
        return False

    print("Digite o nome do jogador 1:")
    jogador1 = input()
    print("Digite o nome do jogador 2:")
    jogador2 = input()
    
    print("\nRegra do jogo:")
    print(f"O jogador {jogador1} vence a rodada se a soma dos números for PAR.")
    print(f"O jogador {jogador2} vence se a soma dos números for ÍMPAR.")
    print("-" * 20)
    
    vencedores_rodada = []

    for _ in range(rodadas):
        while True:
            try:
                print(f"Digite os 2 números para a rodada {_ + 1}:")
                a, b = map(int, input().split())
                break
            except ValueError:
                print("Entrada inválida. Digite dois números inteiros.")

        if (a + b) % 2 == 0:
            vencedores_rodada.append(jogador1)
        else:
            vencedores_rodada.append(jogador2)

    print("\n--- Resultados ---")
    for vencedor in vencedores_rodada:
        print(vencedor)
    print()
    
    return True

def main():
    """Função principal que gerencia os casos de teste."""
    teste = 1
    while True:
        try:
            if not processar_teste(teste):
                break
            teste += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()