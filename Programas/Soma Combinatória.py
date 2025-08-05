def main():
    """
    Função principal que gerencia o fluxo do programa para encontrar
    a soma dos maiores valores combinados de múltiplas listas.
    """
    print("--- Soma de Maiores Combinações ---")
    print("Este programa calcula a soma dos 'k' maiores valores que podem ser formados")
    print("pela soma de um elemento de cada uma das cinco listas fornecidas.")
    
    # Validação e entrada das listas
    while True:
        try:
            p = list(map(int, input("\nDigite os valores para a lista 1, separados por espaço: ").split()))
            m = list(map(int, input("Digite os valores para a lista 2, separados por espaço: ").split()))
            f = list(map(int, input("Digite os valores para a lista 3, separados por espaço: ").split()))
            q = list(map(int, input("Digite os valores para a lista 4, separados por espaço: ").split()))
            b = list(map(int, input("Digite os valores para a lista 5, separados por espaço: ").split()))
            
            total = int(input("Digite quantos dos maiores valores devem ser somados: "))
            
            if total <= 0:
                print("A quantidade a ser somada deve ser maior que zero.")
                continue
            
            # Garante que todas as listas não estão vazias
            if not all([p, m, f, q, b]):
                print("Todas as listas devem conter pelo menos um valor.")
                continue
            
            break
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # A estratégia é combinar as listas em pares, mantendo as maiores somas a cada passo.
    # Isso evita a geração de todas as combinações, que seria muito lento.

    # 1. Combina as duas primeiras listas (p e m) e ordena
    somas_parciais = [val_p + val_m for val_p in p for val_m in m]
    somas_parciais.sort(reverse=True)
    
    # 2. Combina com a terceira lista (f) e reordena
    somas_parciais_2 = [soma + val_f for soma in somas_parciais for val_f in f]
    somas_parciais_2.sort(reverse=True)
    
    # 3. Combina com a quarta lista (q) e reordena
    somas_parciais_3 = [soma + val_q for soma in somas_parciais_2 for val_q in q]
    somas_parciais_3.sort(reverse=True)
    
    # 4. Combina com a quinta lista (b) e reordena
    somas_finais = [soma + val_b for soma in somas_parciais_3 for val_b in b]
    somas_finais.sort(reverse=True)
    
    # Soma os `total` maiores valores da lista final
    result = sum(somas_finais[:total])

    print(f"\nA soma dos {total} maiores valores é: {result}")

if __name__ == "__main__":
    main()