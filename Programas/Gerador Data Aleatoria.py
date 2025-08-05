import random
from datetime import date, timedelta

def main():
    """
    Função principal que gera uma data aleatória entre um período de tempo.
    """
    print("--- Gerador de Data Aleatória ---")
    print("Este programa irá gerar uma data aleatória entre duas datas que você fornecer.")
    
    # Validação e entrada da data inicial
    while True:
        try:
            print("\nDigite a data inicial:")
            dia_inicial = int(input("Dia: "))
            mes_inicial = int(input("Mês: "))
            ano_inicial = int(input("Ano: "))
            data_inicial = date(ano_inicial, mes_inicial, dia_inicial)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite uma data real (Ex: 31/12/2023).")

    # Validação e entrada da data final
    while True:
        try:
            print("\nDigite a data final:")
            dia_final = int(input("Dia: "))
            mes_final = int(input("Mês: "))
            ano_final = int(input("Ano: "))
            data_final = date(ano_final, mes_final, dia_final)
            
            # Garante que a data final não é anterior à inicial
            if data_final < data_inicial:
                print("A data final não pode ser anterior à data inicial. Por favor, digite novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite uma data real.")

    # Calcula a diferença total de dias entre as datas
    diferenca = data_final - data_inicial
    dias_totais = diferenca.days

    # Gera um número aleatório de dias dentro do intervalo
    dias_aleatorios = random.randint(0, dias_totais)

    # Adiciona os dias aleatórios à data inicial para obter a data final aleatória
    data_aleatoria = data_inicial + timedelta(days=dias_aleatorios)

    print(f"\nA data aleatória gerada é: {data_aleatoria.strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()