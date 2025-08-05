def calcular_distancia_manhattan(ponto_inicial, ponto_final):
    """
    Calcula a distância de Manhattan (número de cruzamentos) entre dois pontos.
    """
    xm, ym = ponto_inicial
    xr, yr = ponto_final
    
    distancia_cruzamentos = abs(xr - xm) + abs(yr - ym)
    return distancia_cruzamentos

def main():
    """
    Função principal que gerencia a entrada, cálculo e saída do programa.
    """
    print("\n--- Calculadora de Distância de Manhattan ---")
    print("Este programa calcula a distância entre dois pontos (o número de cruzamentos)")
    print("em um plano que simula o mapa de uma cidade.")

    while True:
        try:
            print("\nDigite as coordenadas do ponto inicial (M), separadas por um espaço (Ex: 2 5):")
            xm, ym = map(int, input().split())
            print("\nDigite as coordenadas do ponto de destino (R), separadas por um espaço (Ex: 8 1):")
            xr, yr = map(int, input().split())
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros para as coordenadas.")

    ponto_m = (xm, ym)
    ponto_r = (xr, yr)
    
    distancia = calcular_distancia_manhattan(ponto_m, ponto_r)
    
    print(f"\nA distância de Manhattan entre os dois pontos é: {distancia} cruzamentos.")

if __name__ == "__main__":
    main()