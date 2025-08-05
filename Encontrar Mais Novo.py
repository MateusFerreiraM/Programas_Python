def ler_pessoas(num_pessoas):
    """
    Lê os nomes e idades de um número específico de pessoas, com validação.
    """
    lista_pessoas = []
    print("\nPreencha os dados das pessoas:")
    for i in range(num_pessoas):
        nome = input(f"Nome da pessoa {i+1}: ")
        while True:
            try:
                idade = int(input(f"Idade de {nome}: "))
                if idade >= 0:
                    lista_pessoas.append([nome, idade])
                    break
                else:
                    print("A idade deve ser um número não negativo.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro para a idade.")
    return lista_pessoas

def imprimir_lista_pessoas(lista):
    """
    Imprime a lista de pessoas de forma organizada.
    """
    for pessoa in lista:
        print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]} anos")

def main():
    """
    Função principal que encontra a pessoa mais nova em uma lista.
    """
    print("--- Encontrar a Pessoa Mais Nova ---")

    # Lê e valida o número de pessoas
    while True:
        try:
            l = int(input("\nQuantas pessoas? "))
            if l > 0:
                break
            else:
                print("O número de pessoas deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    lista_pessoas = ler_pessoas(l)
    
    print("\nLista de pessoas digitadas:")
    imprimir_lista_pessoas(lista_pessoas)

    # elemento de cada lista interna, que é a idade."
    mais_novo = min(lista_pessoas, key=lambda pessoa: pessoa[1])

    print(f"\nO mais novo é {mais_novo[0]} com {mais_novo[1]} anos.")

if __name__ == "__main__":
    main()