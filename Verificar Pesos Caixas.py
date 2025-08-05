def main():
    """
    Função principal que verifica se uma lista de caixas satisfaz as regras.
    """
    print("--- Verificador de Caixas ---")
    print("Este programa verifica se um conjunto de caixas pode ser empilhado,")
    print("seguindo duas regras: a menor caixa não pode ser maior que 8, e a diferença")
    print("entre caixas adjacentes (após a organização) também não pode ser maior que 8.")

    # Lê e valida o número de caixas
    while True:
        try:
            n = int(input("\nDigite o número de caixas: "))
            if n > 0:
                break
            else:
                print("O número de caixas deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    # Lê e valida a lista de caixas
    while True:
        try:
            caixas = list(map(int, input(f"Digite os {n} tamanhos das caixas, separados por espaço: ").split()))
            if len(caixas) == n:
                break
            else:
                print(f"Erro: Forneça exatamente {n} tamanhos de caixas.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # Ordena a lista para fazer a verificação corretamente
    caixas.sort()
    
    possivel = True
    
    # A primeira condição deve ser checada antes do loop
    if caixas[0] > 8:
        possivel = False
    
    # O loop verifica a diferença entre caixas adjacentes
    if possivel:
        for i in range(1, n):
            diferenca = caixas[i] - caixas[i-1]
            if diferenca > 8:
                possivel = False
                break # para de verificar assim que encontra uma falha
    
    if possivel:
        print("Sim")
    else:
        print("Não")

if __name__ == "__main__":
    main()