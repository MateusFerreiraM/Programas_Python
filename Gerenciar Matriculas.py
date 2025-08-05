def main():
    """Função principal que gerencia o fluxo do programa de matrículas."""
    print("\n--- Gerenciamento de Matrículas ---")
    print("Este programa gerencia uma lista de matrículas. Você poderá:")
    print("1. Inserir matrículas iniciais.")
    print("2. Remover matrículas da lista.")
    print("3. Adicionar novas matrículas no início da lista.")
    print("A lista final será limitada a 300 matrículas.")

    print("\n--- Inserção de Matrículas Iniciais ---")
    print("Digite as matrículas iniciais, separadas por espaços:")
    while True:
        try:
            matriculas = list(map(int, input().split()))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    # Loop para remoção de matrículas
    print("\n--- Remoção de Matrículas ---")
    while True:
        continuar_removendo = input("Deseja remover alguma matrícula? (S/N): ").upper()
        if continuar_removendo == "N":
            break
        
        if continuar_removendo == "S":
            try:
                matricula_a_remover = int(input("Digite a matrícula a ser removida: "))
                if matricula_a_remover in matriculas:
                    matriculas.remove(matricula_a_remover)
                    print(f"Matrícula {matricula_a_remover} removida com sucesso.\n")
                else:
                    print(f"A matrícula {matricula_a_remover} não foi encontrada na lista.\n")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a matrícula.")
        else:
            print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.\n")

    # Loop para inserção de novas matrículas
    print("\n--- Inserção de Novas Matrículas no Início ---")
    while True:
        try:
            num_inserir = int(input("Quantas matrículas deseja inserir no início? (ou 0 para sair): "))
            if num_inserir == 0:
                break
            
            for i in range(num_inserir):
                matricula_nova = int(input(f"Digite a {i+1}ª nova matrícula: "))
                matriculas.insert(0, matricula_nova)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")

    # Limita o tamanho da lista a 300 e exibe o resultado final
    matriculas_finais = matriculas[:300]
    print("\n--- Resultado Final ---")
    print(f"A lista final de matrículas (limitada a 300) é: \n{matriculas_finais}\n")

if __name__ == "__main__":
    main()