def solicitar_numeros() -> tuple:
    """
    Solicita três números ao usuário e retorna uma tupla com os valores.

    Retorna:
    tuple: Uma tupla contendo três números fornecidos pelo usuário.
    """
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            num3 = float(input("Digite o terceiro número: "))
            return num1, num2, num3
        except ValueError:
            print("Entrada inválida. Por favor, digite valores numéricos.")

def encontrar_maior(num1: float, num2: float, num3: float) -> float:
    """
    Determina qual é o maior dos três números fornecidos.

    Parâmetros:
    num1 (float): O primeiro número.
    num2 (float): O segundo número.
    num3 (float): O terceiro número.

    Retorna:
    float: O maior número.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

if __name__ == "__main__":
    # Solicitar os números
    num1, num2, num3 = solicitar_numeros()
    
    # Determinar o maior número
    maior = encontrar_maior(num1, num2, num3)
    
    # Exibir o maior número
    print(f"O maior número é: {maior}")
