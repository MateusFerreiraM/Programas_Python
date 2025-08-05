def calcula_status(nota):
    """
    Classifica a nota de um aluno em Aprovado, Reprovado ou Verificação Suplementar.
    
    Args:
        nota (float): A nota do aluno.
        
    Returns:
        str: O status do aluno.
    """
    if nota > 6:
        return "Aprovado"
    elif nota < 4:
        return "Reprovado"
    else:
        return "Verificação Suplementar"

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Verificador de Status Acadêmico ---")
    print("Este programa classifica a nota de um aluno com base em um critério simples.")
    
    # Adiciona um loop de validação para a entrada
    while True:
        try:
            media = float(input('Digite a nota do aluno: '))
            break  # Sai do loop se a entrada for um número válido
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            
    status = calcula_status(media)
    
    print(f"O aluno está: {status}")

if __name__ == "__main__":
    main()