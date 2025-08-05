def contar_ocorrencias(texto, palavra_alvo):
    """
    Conta o número de vezes que uma palavra aparece em um texto, ignorando maiúsculas e minúsculas.
    
    Args:
        texto (list): Uma lista de palavras.
        palavra_alvo (str): A palavra a ser procurada.
        
    Returns:
        int: O número de ocorrências.
    """
    # Converte a palavra alvo para maiúsculas para uma comparação sem distinção de caso
    palavra_alvo_upper = palavra_alvo.upper()
    
    # Usa uma list comprehension e sum() para contar de forma concisa e eficiente
    return sum(1 for palavra in texto if palavra.upper() == palavra_alvo_upper)

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    print("--- Contador de Palavras no Texto ---")
    print("Este programa conta quantas vezes uma palavra específica aparece em uma frase.")
    
    # Lê a frase e a palavra com prompts claros
    texto_input = input("\nDigite a frase (palavras separadas por espaço): ")
    palavra_input = input("Digite a palavra que você quer contar: ")
    
    # .split() sem argumento lida melhor com múltiplos espaços
    texto_lista = texto_input.split()
    
    # Chama a função para contar
    ocorrencias = contar_ocorrencias(texto_lista, palavra_input)
    
    # Imprime o resultado usando uma f-string
    print(f"\nA palavra '{palavra_input}' aparece {ocorrencias} vez(es) no texto.")

if __name__ == "__main__":
    main()