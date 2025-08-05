def calcula_media(valores):
    """Calcula a média de uma lista de números de forma concisa."""
    if not valores:
        return 0
    return sum(valores) / len(valores)

def calcula_centroide(coordenadas):
    """
    Calcula o centróide de um conjunto de pontos a partir de uma lista
    única de coordenadas [x1, y1, x2, y2, ...].
    
    Args:
        coordenadas (list): A lista de coordenadas dos pontos.
        
    Returns:
        tuple: As coordenadas (media_x, media_y) do centróide.
    """
    # Valida se o número de coordenadas é par.
    if len(coordenadas) % 2 != 0:
        raise ValueError("O número de coordenadas deve ser par (x e y para cada ponto).")
    
    # Extrai as coordenadas X e Y em listas separadas
    lista_x = coordenadas[0::2]
    lista_y = coordenadas[1::2]
    
    media_x = calcula_media(lista_x)
    media_y = calcula_media(lista_y)
    
    return media_x, media_y

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("\n--- Calculadora de Centróide de Pontos ---")
    print("Este programa calcula o ponto central (centróide) de um conjunto de pontos.")
    print("O centróide é a média das coordenadas X e Y de todos os pontos.")

    while True:
        try:
            coordenadas_input = input("\nDigite as coordenadas dos pontos (Ex: x1 y1 x2 y2): ")
            coordenadas = list(map(float, coordenadas_input.split()))
            
            # Valida se a quantidade de coordenadas é par
            if len(coordenadas) % 2 == 0:
                break
            else:
                print("Erro: O número de coordenadas deve ser par (cada ponto tem um X e um Y).")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros ou decimais.")

    try:
        centroide_x, centroide_y = calcula_centroide(coordenadas)
        print(f"\nO centróide dos pontos é: ({centroide_x:.2f}, {centroide_y:.2f})")
    except ValueError as e:
        print(f"\nErro no cálculo: {e}")

if __name__ == "__main__":
    main()