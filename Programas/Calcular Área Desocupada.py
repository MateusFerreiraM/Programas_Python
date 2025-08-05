import math

def main():
    """
    Função principal que calcula a área desocupada de um retângulo com
    um círculo no interior.
    """
    print("\n--- Calculadora de Área Desocupada ---")
    print("Este programa calcula a área de um retângulo e subtrai a área de um círculo.")

    # Lê e valida as dimensões do retângulo
    while True:
        try:
            largura = float(input("\nDigite a largura do retângulo: "))
            comprimento = float(input("Digite o comprimento do retângulo: "))
            if largura > 0 and comprimento > 0:
                break
            else:
                print("As dimensões devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
    
    # Lê e valida o raio do círculo
    while True:
        try:
            raio = float(input("\nDigite o raio do círculo: "))
            if raio > 0:
                break
            else:
                print("O raio deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    # Calcula as áreas
    area_retangulo = largura * comprimento
    area_circulo = math.pi * (raio ** 2)
    
    # Calcula a área desocupada
    area_desocupada = area_retangulo - area_circulo

    # Exibe o resultado com formatação
    print(f"\n- Área do retângulo: {area_retangulo:.2f}")
    print(f"- Área do círculo:   {area_circulo:.2f}")
    
    if area_desocupada > 0:
        print(f"\nA área desocupada é: {area_desocupada:.2f}")
    else:
        print("\nA área do círculo é maior ou igual à área do retângulo.")


if __name__ == "__main__":
    main()