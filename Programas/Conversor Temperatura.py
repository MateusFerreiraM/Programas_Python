def converter_temperatura(valor, unidade_origem):
    """
    Converte uma temperatura entre as escalas Celsius, Fahrenheit e Kelvin.
    
    Args:
        valor (float): O valor da temperatura a ser convertida.
        unidade_origem (str): A unidade de origem ('C', 'F' ou 'K').
        
    Returns:
        tuple: Uma tupla contendo os valores convertidos ou None se a entrada for inválida.
    """
    if unidade_origem.upper() == 'C':
        # Converte de Celsius
        if valor < -273.15:
            return None, "Celsius abaixo do zero absoluto."
        fahrenheit = (valor * 9/5) + 32
        kelvin = valor + 273.15
        return (fahrenheit, "Fahrenheit"), (kelvin, "Kelvin")
        
    elif unidade_origem.upper() == 'F':
        # Converte de Fahrenheit
        if valor < -459.67:
            return None, "Fahrenheit abaixo do zero absoluto."
        celsius = (valor - 32) * 5/9
        kelvin = celsius + 273.15
        return (celsius, "Celsius"), (kelvin, "Kelvin")
        
    elif unidade_origem.upper() == 'K':
        # Converte de Kelvin
        if valor < 0:
            return None, "Kelvin abaixo do zero absoluto."
        celsius = valor - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return (celsius, "Celsius"), (fahrenheit, "Fahrenheit")
        
    else:
        return None, "Unidade de origem inválida."

def main():
    """Função principal que gerencia o fluxo do conversor."""
    print("--- Conversor Completo de Temperatura ---")
    print("Este programa converte uma temperatura entre Celsius, Fahrenheit e Kelvin.")
    
    while True:
        # Pede a unidade de origem e valida
        unidade_origem = input("\nDigite a unidade de origem (C, F ou K): ").upper()
        if unidade_origem not in ['C', 'F', 'K']:
            print("Unidade inválida. Por favor, digite C, F ou K.")
            continue
            
        # Pede o valor e valida
        try:
            valor = float(input(f"Digite o valor da temperatura em {unidade_origem}: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue
            
        # Realiza a conversão
        resultado1, resultado2_ou_erro = converter_temperatura(valor, unidade_origem)
        
        if resultado1 is None:
            print(f"Erro: {resultado2_ou_erro}")
        else:
            valor1, unidade1 = resultado1
            valor2, unidade2 = resultado2_ou_erro
            
            print(f"\n{valor:.2f}°{unidade_origem} corresponde a:")
            print(f"{valor1:.2f}°{unidade1}")
            print(f"{valor2:.2f}°{unidade2}")

        # Pergunta se o usuário quer continuar
        continuar = input("\nDeseja fazer outra conversão? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()