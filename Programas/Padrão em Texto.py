def encontrar_ocorrencias(texto, padrao):
    """
    Conta quantas janelas de 3 caracteres no texto contêm todos os
    caracteres do padrão.
    
    Args:
        texto (list): A lista de caracteres para busca.
        padrao (list): A lista de caracteres a serem encontrados.
        
    Returns:
        int: O número de janelas que correspondem ao padrão.
    """
    contagem = 0
    tamanho_padrao = len(padrao)

    # A busca é feita em janelas de 3 caracteres, como sugerido pelo código original.
    # O loop vai até o ponto em que a janela de 3 caracteres se encaixa.
    for i in range(len(texto) - 2):
        janela = texto[i:i+3]
        
        # Converte a janela e o padrão para conjuntos para verificar se
        # o padrão está contido na janela de forma eficiente.
        # Usa `.issubset` para verificar se todos os caracteres do padrão estão na janela.
        if set(padrao).issubset(set(janela)):
            contagem += 1
            
    return contagem

def main():
    """Função principal que gerencia o fluxo do programa."""
    print("--- Contador de Padrão em Cadeia ---")
    print("Este programa conta quantas sequências de 3 caracteres (janelas) da primeira")
    print("cadeia contêm todos os caracteres da segunda cadeia.")

    # Lê e converte as entradas para listas de caracteres
    cadeia_a = list(input("Digite a cadeia de texto principal: "))
    cadeia_b = list(input("Digite a cadeia de caracteres a ser buscada (padrão): "))
    
    # A lógica original do seu código implica que a busca é por um padrão de 3 caracteres.
    # Se o padrão tiver um tamanho diferente, a lógica deve ser ajustada.
    # Aqui, garantimos que o padrão não é maior que a janela.
    if len(cadeia_b) > 3:
        print("Aviso: O padrão de busca é maior que a janela de 3 caracteres. Nenhum resultado será encontrado.")
        resultado = 0
    else:
        resultado = encontrar_ocorrencias(cadeia_a, cadeia_b)

    print(f"\nO número de ocorrências do padrão é: {resultado}")

if __name__ == "__main__":
    main()