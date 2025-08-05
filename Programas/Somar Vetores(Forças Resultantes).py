def ler_vetor(nome_vetor, num_dimensoes=3):
    """
    Lê as componentes de um vetor do usuário, com validação de entrada.
    """
    vetor = []
    print(f"\nDigite as componentes do {nome_vetor}:")
    for i in range(num_dimensoes):
        while True:
            try:
                valor = float(input(f"Componente {i+1}: "))
                vetor.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    return vetor

def main():
    """
    Função principal que soma dois vetores de 3 dimensões.
    """
    print("--- Calculadora de Soma de Vetores ---")
    print("Este programa soma dois vetores de 3 dimensões (x, y, z).")

    # Lê as componentes dos dois vetores
    vetor1 = ler_vetor("Vetor 1")
    vetor2 = ler_vetor("Vetor 2")

    # Realiza a soma dos vetores de forma concisa usando list comprehension e zip
    forca_resultante = [v1 + v2 for v1, v2 in zip(vetor1, vetor2)]

    print(f"\nAs forças resultantes são: {forca_resultante}")

if __name__ == "__main__":
    main()