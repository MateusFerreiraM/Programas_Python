def main():
    """
    Função principal que gera a tabuada de um número.
    """
    print("--- Gerador de Tabuada ---")

    # Lê e valida o número para a tabuada
    while True:
        try:
            tabuada = int(input("Digite o número para gerar a tabuada: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print(f"\nTabuada de {tabuada}:")
    for count in range(1, 11): # O loop vai de 1 a 10
        # Usa uma f-string para uma formatação mais clara
        print(f"{tabuada} x {count} = {tabuada * count}")

if __name__ == "__main__":
    main()