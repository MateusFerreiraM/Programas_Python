def verificar_propriedade(numeros):
    """
    Verifica se uma lista de três números inteiros atende a uma condição específica.

    Args:
        numeros (list): Uma lista contendo três números inteiros.

    Returns:
        str: "S" se a condição for atendida, "N" caso contrário.
    """
    if len(numeros) != 3:
        return "N"
    
    numeros.sort()

    # A condição verifica se a soma dos dois menores é igual ao maior,
    # ou se existem dois números iguais na lista.
    if (numeros[0] + numeros[1] == numeros[2]) or (numeros[0] == numeros[1]) or (numeros[1] == numeros[2]):
        return "Sim"
    else:
        return "Não"

def main():
    """Função principal que gerencia a entrada e a saída."""
    print("--- Verificação de Triplos ---")
    print("Este programa lê três números e verifica se a soma dos dois menores")
    print("é igual ao maior, ou se há dois números iguais entre eles.")
    print("\nDigite três números inteiros, separados por um espaço:")
    
    while True:
        try:
            numeros = list(map(int, input().split()))
            if len(numeros) != 3:
                print("Por favor, digite exatamente três números.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

    resultado = verificar_propriedade(numeros)
    print(f"\nResultado: {resultado}")

if __name__ == "__main__":
    main()