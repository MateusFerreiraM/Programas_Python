def main():
    """
    Função principal que conta quantos valores únicos existem em uma lista.
    """
    print("--- Contador de Valores Únicos ---")

    lista = []
    
    for i in range(10):
        while True:
            try:
                elm = int(input(f"Digite o {i+1}º valor: "))
                lista.append(elm)
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    
    # Converte a lista para um set, que armazena apenas valores únicos.
    # Em seguida, calcula o tamanho do set.
    valores_unicos = set(lista)
    contador_unicos = len(valores_unicos)

    print(f"\nLista digitada: {lista}")
    print(f"A lista possui {contador_unicos} valores únicos.")

if __name__ == "__main__":
    main()