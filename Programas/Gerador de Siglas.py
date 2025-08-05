def gerar_sigla(frase):
    """
    Gera uma sigla a partir de uma frase, pegando a primeira letra de cada palavra.
    
    Args:
        frase (str): A frase de entrada.
        
    Returns:
        str: A sigla gerada.
    """
    # Usa split() para dividir a frase em palavras
    palavras = frase.split()
    
    # Usa um gerador de expressão com join para construir a string de forma eficiente.
    sigla = "".join(palavra[0].upper() for palavra in palavras if palavra)
    
    return sigla

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Gerador de Siglas ---")
    print("Este programa cria uma sigla a partir da primeira letra de cada palavra em uma frase.")

    # Lê o número de frases a serem processadas com validação
    while True:
        try:
            num_frases = int(input("\nDigite o número de frases que você irá processar: "))
            if num_frases >= 0:
                break
            print("O número de frases deve ser não negativo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    print("\nDigite as frases, uma por linha:")
    
    for _ in range(num_frases):
        frase = input()
        sigla_gerada = gerar_sigla(frase)
        print(sigla_gerada)
        

if __name__ == "__main__":
    main()