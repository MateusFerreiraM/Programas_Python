import math

def calcular_distancia(ponto1, ponto2):
    """
    Calcula a distância euclidiana entre dois pontos (x, y).
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def classificar_triangulo(a, b, c):
    """
    Classifica um triângulo com base nos comprimentos de seus lados.
    """
    # Adiciona uma pequena tolerância para lidar com imprecisões de ponto flutuante
    tol = 1e-9

    # Verifica se os pontos formam um triângulo válido (desigualdade triangular)
    if not (a + b > c and a + c > b and b + c > a):
        return "O Triângulo não existe!"

    # Classifica o triângulo
    if abs(a - b) < tol and abs(b - c) < tol:
        return "O Triângulo é equilátero!"
    elif abs(a - b) < tol or abs(b - c) < tol or abs(a - c) < tol:
        return "O Triângulo é isósceles!"
    else:
        return "O Triângulo é escaleno!"

def main():
    """
    Função principal que gerencia a entrada e a classificação do triângulo.
    """
    print("--- Classificador de Triângulos ---")
    
    # Lê e valida as coordenadas
    while True:
        try:
            x1, y1 = map(float, input("\nDigite as coordenadas do ponto 1 (x1 y1): ").split())
            x2, y2 = map(float, input("Digite as coordenadas do ponto 2 (x2 y2): ").split())
            x3, y3 = map(float, input("Digite as coordenadas do ponto 3 (x3 y3): ").split())
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

    # Calcula os comprimentos dos lados
    ab = calcular_distancia((x1, y1), (x2, y2))
    ac = calcular_distancia((x1, y1), (x3, y3))
    bc = calcular_distancia((x2, y2), (x3, y3))

    # Classifica e imprime o resultado
    resultado = classificar_triangulo(ab, ac, bc)
    print(f"\n{resultado}")

if __name__ == "__main__":
    main()