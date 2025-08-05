def main():
    """
    Função principal que gerencia o fluxo de processamento da lista.
    """
    print("--- Processador de Listas ---")
    
    # Lê e valida o número de valores
    while True:
        try:
            num_valores = int(input("\nDigite quantos valores você quer processar: "))
            if num_valores > 0:
                break
            print("O número de valores deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    vet = []
    print(f"Digite os {num_valores} valores:")
    for i in range(num_valores):
        while True:
            try:
                valor = int(input(f"Valor {i+1}: "))
                vet.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    
    # Filtra apenas os números inteiros positivos
    vetPos = [item for item in vet if item > 0]
    
    # Remove as duplicatas de forma eficiente usando um set
    # O set armazena apenas valores únicos.
    # A ordem pode ser perdida neste processo.
    vetSemdup = list(set(vetPos))

    print(f"\nLista Original: {vet}")
    print(f"Lista de Positivos: {vetPos}")
    print(f"Lista Sem Duplicatas: {vetSemdup}")

if __name__ == "__main__":
    main()