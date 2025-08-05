def main():
    """
    Função principal que gerencia o fluxo do programa de verificação de duplicatas.
    """
    print("--- Verificador de Coordenadas Duplicadas ---")
    print("Este programa lê uma série de coordenadas (x, y) e verifica se há duplicatas.")
    
    # Lê e valida o número de coordenadas a serem processadas
    while True:
        try:
            n = int(input("\nDigite o número de coordenadas para verificar: "))
            if n > 0:
                break
            else:
                print("O número deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    # Usamos um 'set' para armazenar as coordenadas já vistas.
    # A busca em um set é muito mais rápida do que em uma lista.
    coordenadas_vistas = set()
    raios = 0 # 0 para sem duplicatas, 1 para com duplicatas
    
    print("Digite as coordenadas x e y, uma por linha:")
    
    for i in range(n):
        while True:
            try:
                x, y = map(int, input(f"Coordenada {i+1}: ").split())
                break
            except ValueError:
                print("Entrada inválida. Digite dois números inteiros separados por espaço.")
        
        # A coordenada é armazenada como uma tupla (x, y) no set
        if (x, y) in coordenadas_vistas:
            raios = 1 # Duplicata encontrada!
            break # Encerra o loop assim que uma duplicata é encontrada
        else:
            coordenadas_vistas.add((x, y))
            
    if raios == 1:
        print("\n1")
        print("Ponto duplicado encontrado.")
    else:
        print("\n0")
        print("Nenhum ponto duplicado encontrado.")

if __name__ == "__main__":
    main()