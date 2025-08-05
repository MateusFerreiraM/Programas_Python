# Cria uma lista vazia para armazenar os valores inteiros
vet = []

print("Digite 5 números inteiros:")
for i in range(5):
    while True:
        try:
            valor = int(input(f'Valor {i+1}: '))
            vet.append(valor)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

while True:
    try:
        x = int(input("\nDigite um número inteiro para ser procurado na lista: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Tenta encontrar o valor na lista e mostra sua posição
try:
    posicao = vet.index(x)
    print(f"\nO número {x} foi encontrado na posição {posicao+1}.")
except ValueError:
    # Caso o valor não seja encontrado, exibe uma mensagem
    print(f"\nO número {x} não foi encontrado na lista.")