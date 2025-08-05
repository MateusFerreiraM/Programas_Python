def converter_para_minutos(horario_str):
    """
    Converte uma string de horário "hh:mm" para o total de minutos.
    Retorna None se o formato for inválido.
    """
    try:
        hora, minuto = map(int, horario_str.split(':'))
        if not (0 <= hora <= 23 and 0 <= minuto <= 59):
            return None
        return hora * 60 + minuto
    except (ValueError, IndexError):
        return None

def main():
    """
    Função principal que calcula a duração de uma viagem e o fuso horário.
    """
    print("--- Calculadora de Viagem ---")
    print("Este programa calcula a duração de uma viagem e a diferença de fuso horário.")
    print("Formato de entrada esperado: 'hh:mm hh:mm hh:mm hh:mm'")
    
    while True:
        try:
            pA_str, cB_str, pB_str, cA_str = input("\nDigite os horários (Partida A, Chegada B, Partida B, Chegada A): ").split()
            
            pA = converter_para_minutos(pA_str)
            cB = converter_para_minutos(cB_str)
            pB = converter_para_minutos(pB_str)
            cA = converter_para_minutos(cA_str)
            
            if None not in [pA, cB, pB, cA]:
                break
            else:
                print("Formato de horário inválido. Use 'hh:mm' (Ex: 10:30).")
        except ValueError:
            print("Entrada inválida. Digite 4 horários separados por espaço.")

    # Sua lógica para calcular a duração e o fuso horário
    duracao_total = cB + cA - (pA + pB)
    duracao_total %= (60 * 24)
    duracao = duracao_total // 2

    fuso_horario = (cB - (pA + duracao)) // 60
    while fuso_horario < -11:
        fuso_horario += 24
    while fuso_horario > 12:
        fuso_horario -= 24
        
    print(f"\nA duração da viagem é de {duracao} minutos.")
    print(f"O fuso horário de B em relação a A é de {fuso_horario} horas.")
    

if __name__ == "__main__":
    main()