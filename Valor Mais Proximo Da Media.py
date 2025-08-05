def main():
    """
    Função principal que encontra o valor mais próximo da média em uma lista.
    """
    print("--- Encontrador de Valor Mais Próximo da Média ---")
    
    # Lê e valida a lista de entrada
    while True:
        try:
            vet = list(map(float, input("Digite os valores da lista (separados por espaço): ").split()))
            if not vet:
                print("A lista não pode estar vazia.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
    
    # Calcula a média de forma concisa
    media = sum(vet) / len(vet)
    
    # Inicializa a variável 'menor' com o primeiro elemento da lista,
    # o que garante que ela sempre terá um valor válido para começar a comparação.
    menor_diferenca = abs(media - vet[0])
    valor_proximo = vet[0]

    # Encontra o valor mais próximo da média
    for i in range(1, len(vet)):
        diferenca_atual = abs(media - vet[i])
        
        if diferenca_atual < menor_diferenca:
            menor_diferenca = diferenca_atual
            valor_proximo = vet[i]
    
    print(f"\nA média do vetor é: {media:.2f}")
    print(f"O valor mais próximo da média é: {valor_proximo}")

if __name__ == "__main__":
    main()