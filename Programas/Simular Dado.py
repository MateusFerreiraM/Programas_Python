import random

def main():
    """
    Função principal que simula lançamentos de um dado e calcula a porcentagem
    de ocorrência de uma face específica.
    """
    print("--- Simulador de Lançamento de Dados ---")
    
    # Define os parâmetros da simulação
    while True:
        try:
            num_lancamentos = int(input("\nDigite o número de lançamentos a serem simulados: "))
            face_alvo = int(input("Digite a face que você quer contar (de 1 a 6): "))
            if num_lancamentos > 0 and 1 <= face_alvo <= 6:
                break
            else:
                print("Entrada inválida. O número de lançamentos deve ser positivo, e a face deve ser de 1 a 6.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # Simula os lançamentos e conta as ocorrências
    contagem = 0
    resultados_lancamentos = []
    for _ in range(num_lancamentos):
        lancamento = random.randint(1, 6)
        resultados_lancamentos.append(lancamento)
        if lancamento == face_alvo:
            contagem += 1

    # Calcula a porcentagem
    porcentagem = (contagem / num_lancamentos) * 100

    # Imprime o resultado formatado
    print(f"\nResultados dos lançamentos (primeiros 10): {resultados_lancamentos[:10]}...")
    print(f"A face {face_alvo} apareceu {contagem} vez(es) em {num_lancamentos} lançamentos.")
    print(f"Isso representa uma porcentagem de {porcentagem:.2f}%.")

if __name__ == "__main__":
    main()