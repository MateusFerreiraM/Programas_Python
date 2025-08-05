def main():
    """
    Função principal que formata um número com zeros à esquerda.
    """
    print("--- Formatador de Números ---")
    
    # Lê e valida o número
    while True:
        try:
            n = int(input("\nDigite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Lê e valida a quantidade de dígitos
    while True:
        try:
            dig = int(input("Digite a quantidade de dígitos desejada: "))
            if dig > 0:
                break
            else:
                print("A quantidade de dígitos deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Usa uma f-string para formatar o número com zeros à esquerda
    # O '0' indica preenchimento com zeros.
    # O 'd' indica que é um número inteiro.
    saida_formatada = f"{n:0{dig}d}"
    
    # Outra forma concisa seria usando o método zfill():
    # saida_formatada = str(n).zfill(dig)
    
    print(f"\nNúmero original: {n}")
    print(f"Saída formatada: {saida_formatada}")

if __name__ == "__main__":
    main()