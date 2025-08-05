import sys
import random

def main():
    """
    Função principal que simula uma corrida e exibe as estatísticas.
    """
    print("--- Simulador de Corrida ---")

    # Lê e valida o número de corredores e voltas
    while True:
        try:
            num_corredores = int(input("Digite o número de corredores: "))
            num_voltas = int(input("Digite o número de voltas: "))
            if num_corredores > 0 and num_voltas > 0:
                break
            print("Entrada inválida. Os valores devem ser positivos.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")

    corredores = []
    melhor_volta = [None, sys.maxsize, -1]
    soma_tempos_por_volta = [0] * num_voltas
    classificacao = []

    for i in range(num_corredores):
        nome = input(f"Digite o nome do corredor {i+1}: ")
        
        # Gera tempos aleatórios para cada corredor
        tempos_voltas = [random.randint(500, 1000) for _ in range(num_voltas)]
        
        # Acumula os tempos para calcular a média de cada volta
        for j in range(num_voltas):
            soma_tempos_por_volta[j] += tempos_voltas[j]
        
        # Armazena os dados do corredor
        classificacao.append([sum(tempos_voltas), nome])
        tempos_voltas.insert(0, nome)
        corredores.append(tempos_voltas)

        # Encontra a melhor volta individual de cada corredor
        melhor_volta_corredor = min(tempos_voltas[1:]) 
        if melhor_volta_corredor < melhor_volta[1]:
            melhor_volta = [nome, melhor_volta_corredor, tempos_voltas.index(melhor_volta_corredor)]

    # calcula a média após o loop principal
    medias_voltas = [soma / num_corredores for soma in soma_tempos_por_volta]
    
    # Ordena a classificação dos corredores pelo tempo total
    classificacao.sort()
    
    # Encontra a melhor média de volta (menor tempo)
    melhor_media_volta = medias_voltas.index(min(medias_voltas)) + 1

    print("\n--- Resultados da Corrida ---")
    print(f"A melhor volta de todas foi a de {melhor_volta[0]} na volta {melhor_volta[2]}.")
    print("\nClassificação Geral:")
    for i in range(num_corredores):
        print(f"{i+1}º - {classificacao[i][1]} (Tempo Total: {classificacao[i][0]}s)")
    
    print(f"\nA volta com a média mais rápida foi a {melhor_media_volta}ª.")
    
if __name__ == "__main__":
    main()