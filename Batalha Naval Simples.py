def criar_tabuleiro(linhas, colunas, valor_padrao="A"):
    """
    Cria e retorna um tabuleiro de Batalha Naval preenchido com um valor padrão.
    """
    return [[valor_padrao for _ in range(colunas)] for _ in range(linhas)]

def exibir_tabuleiro(tabuleiro):
    """
    Imprime o tabuleiro de forma formatada.
    """
    for linha in tabuleiro:
        print(" ".join(linha))

def posicionar_navios(tabuleiro, navios):
    """
    Posiciona navios no tabuleiro com base em uma lista de coordenadas.
    """
    # A lista de navios deve ser uma sequência de pares (linha, coluna)
    for i in range(0, len(navios), 2):
        linha, coluna = navios[i], navios[i+1]
        
        # Verifica se as coordenadas estão dentro dos limites do tabuleiro
        if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
            tabuleiro[linha][coluna] = "N"
        else:
            print(f"Aviso: Coordenada de navio inválida ({linha}, {coluna}) ignorada.")

def testa_jogada(tabuleiro, posicao_tiro):
    """
    Verifica se um tiro acertou um navio em uma determinada posição.
    Retorna "Sim" se acertou e "Não" se errou.
    """
    try:
        linha, coluna = posicao_tiro
        # Verifica se a posição do tiro está dentro dos limites do tabuleiro
        if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
            if tabuleiro[linha][coluna] == "N":
                return "Sim"
            else:
                return "Não"
        else:
            return "Tiro fora do tabuleiro"
    except (IndexError, ValueError):
        return "Coordenadas do tiro inválidas"

def main():
    """
    Função principal que gerencia o fluxo do jogo de Batalha Naval.
    """
    print("--- Jogo de Batalha Naval Simplificado ---")

    # --- Configuração do tabuleiro ---
    while True:
        try:
            l, c = map(int, input("Digite o número de linhas e colunas, separados por um espaço: ").split())
            if l > 0 and c > 0:
                break
            else:
                print("As dimensões devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    tabuleiro = criar_tabuleiro(l, c)
    print("\nTabuleiro inicial (A = Água):")
    exibir_tabuleiro(tabuleiro)

    # --- Posicionamento dos navios ---
    while True:
        try:
            print("\nDigite as coordenadas dos navios (linha coluna linha coluna...):")
            print("Exemplo: '0 1 2 3' posicionaria navios em (0,1) e (2,3).")
            navios = list(map(int, input().split()))
            if len(navios) % 2 == 0:
                break
            else:
                print("Número de coordenadas ímpar. Cada navio precisa de duas coordenadas.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros para as coordenadas.")

    posicionar_navios(tabuleiro, navios)
    print("\nTabuleiro com navios (N = Navio):")
    exibir_tabuleiro(tabuleiro)

    # --- Realização do tiro ---
    while True:
        try:
            tiro = list(map(int, input("\nDigite as coordenadas do seu tiro (linha coluna): ").split()))
            if len(tiro) == 2:
                break
            else:
                print("Por favor, digite duas coordenadas para o tiro.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    # --- Verificação do tiro e resultado ---
    resultado = testa_jogada(tabuleiro, tiro)
    print(f"\nResultado do tiro: {resultado}")

if __name__ == "__main__":
    main()