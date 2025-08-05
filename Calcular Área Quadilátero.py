from math import sqrt

def ler_ponto(nome_ponto):
    """
    Lê as coordenadas de um ponto em centímetros (cm), com validação de entrada.
    """
    while True:
        try:
            coordenadas = list(map(float, input(f"Digite as coordenadas do ponto {nome_ponto} (em cm, Ex: x y): ").split()))
            if len(coordenadas) == 2:
                return coordenadas
            else:
                print("Por favor, digite exatamente duas coordenadas (x e y).")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

def calcular_distancia(ponto1, ponto2):
    """
    Calcula a distância entre dois pontos no plano cartesiano.
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calcular_area_triangulo(lado1, lado2, lado3):
    """
    Calcula a área de um triângulo usando a fórmula de Heron.
    """
    semiperimetro = (lado1 + lado2 + lado3) / 2
    
    try:
        area = sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
        return area
    except ValueError:
        return 0.0

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    print("--- Cálculo da Área de um Quadrilátero ---")
    print("Este programa calcula a área de um quadrilátero a partir de 4 vértices,")
    print("usando a unidade de medida em centímetros (cm).")
    
    ponto_a = ler_ponto('A')
    ponto_b = ler_ponto('B')
    ponto_c = ler_ponto('C')
    ponto_d = ler_ponto('D')

    lado_ab = calcular_distancia(ponto_a, ponto_b)
    lado_bc = calcular_distancia(ponto_b, ponto_c)
    lado_cd = calcular_distancia(ponto_c, ponto_d)
    lado_da = calcular_distancia(ponto_d, ponto_a)
    diagonal_ac = calcular_distancia(ponto_a, ponto_c)

    area_triangulo1 = calcular_area_triangulo(lado_ab, lado_bc, diagonal_ac)
    area_triangulo2 = calcular_area_triangulo(diagonal_ac, lado_cd, lado_da)

    area_total = area_triangulo1 + area_triangulo2

    print(f"\nA área total do quadrilátero é: {area_total:.2f} cm².")

if __name__ == "__main__":
    main()