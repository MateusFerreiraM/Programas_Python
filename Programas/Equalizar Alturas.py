def main():
    """
    Função principal que gerencia o fluxo do programa para equalizar uma lista.
    """
    print("--- Equalizador de Alturas ---")
    print("Este programa calcula os movimentos mínimos para que todos os elementos")
    print("de uma lista atinjam uma altura alvo, ajustando elementos adjacentes.")

    # Lê e valida o número de elementos e a altura alvo
    while True:
        try:
            num_elementos, altura_alvo = map(int, input("\nDigite o número de elementos e a altura alvo: ").split())
            if num_elementos > 0:
                break
            else:
                print("O número de elementos deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite dois números inteiros.")

    # Lê e valida a lista de alturas
    while True:
        try:
            alturas = list(map(int, input(f"Digite as {num_elementos} alturas, separadas por espaços: ").split()))
            if len(alturas) == num_elementos:
                break
            else:
                print(f"Erro: Forneça exatamente {num_elementos} alturas.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
    
    movimentos_totais = 0
    
    # O loop deve começar do primeiro elemento (índice 0) até o penúltimo
    # A correção de cada elemento é "passada" para o próximo
    for i in range(num_elementos - 1):
        diferenca = altura_alvo - alturas[i]
        
        # O número de movimentos é a soma dos ajustes
        movimentos_totais += abs(diferenca)
        
        # O ajuste é aplicado ao elemento atual (para equalizá-lo)
        # e ao próximo (que será o alvo da próxima iteração)
        alturas[i] += diferenca
        alturas[i+1] += diferenca
    
    # Após o loop, o último elemento deve estar na altura alvo.
    # Se não estiver, significa que é impossível equalizar a lista.
    if alturas[num_elementos-1] == altura_alvo:
        print(f"\nO número total de movimentos necessários é: {movimentos_totais}")
    else:
        print("\nÉ impossível equalizar a lista com a altura alvo. (-1)")

if __name__ == "__main__":
    main()