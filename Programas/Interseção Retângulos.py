def verificar_intersecao_retangulos(retangulo1, retangulo2):
    """
    Verifica se dois retângulos se intersectam.

    Args:
        retangulo1 (tuple): Coordenadas do primeiro retângulo (x0, y0, x1, y1).
        retangulo2 (tuple): Coordenadas do segundo retângulo (x2, y2, x3, y3).

    Returns:
        bool: True se os retângulos se intersectam, False caso contrário.
    """
    x0, y0, x1, y1 = retangulo1
    x2, y2, x3, y3 = retangulo2

    # A lógica correta para interseção é:
    # Os retângulos se intersectam se e somente se
    # eles se sobrepõem no eixo X E no eixo Y.
    #
    # Sobreposição no eixo X:
    # (O lado esquerdo do R1 está à esquerda do lado direito do R2)
    # E (O lado direito do R1 está à direita do lado esquerdo do R2)
    sobreposicao_x = (x0 < x3) and (x1 > x2)

    # Sobreposição no eixo Y:
    # (O lado de baixo do R1 está abaixo do lado de cima do R2)
    # E (O lado de cima do R1 está acima do lado de baixo do R2)
    sobreposicao_y = (y0 < y3) and (y1 > y2)
    
    return sobreposicao_x and sobreposicao_y

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("\n--- Verificador de Interseção de Retângulos ---")
    print("Este programa verifica se dois retângulos no plano cartesiano se sobrepõem.")

    # Lê e valida as coordenadas do primeiro retângulo
    while True:
        try:
            coords1 = list(map(int, input("\nDigite x0, y0, x1, y1 para o 1º retângulo: ").split()))
            if len(coords1) == 4:
                retangulo1 = tuple(coords1)
                break
            else:
                print("Entrada inválida. Digite exatamente 4 números inteiros.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # Lê e valida as coordenadas do segundo retângulo
    while True:
        try:
            coords2 = list(map(int, input("Digite x2, y2, x3, y3 para o 2º retângulo: ").split()))
            if len(coords2) == 4:
                retangulo2 = tuple(coords2)
                break
            else:
                print("Entrada inválida. Digite exatamente 4 números inteiros.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # Verifica a interseção e exibe o resultado
    if verificar_intersecao_retangulos(retangulo1, retangulo2):
        print("\nOs retângulos se intersectam.")
    else:
        print("\nOs retângulos não se intersectam.")

if __name__ == "__main__":
    main()