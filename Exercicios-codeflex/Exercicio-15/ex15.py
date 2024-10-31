def solicitar_numero(prompt):
    """
    Solicita um número ao usuário e valida a entrada.

    **Lógica:**
    - Utiliza um loop `while True` para garantir que o usuário digite um número válido.
    - Emprega um `try-except` para tratar possíveis erros de conversão para float.
    - Retorna o número convertido para float.

    Args:
        prompt (str): Mensagem a ser exibida para o usuário.

    Returns:
        float: Número inserido pelo usuário.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def solicitar_operacao():
    """
    Solicita a operação matemática desejada pelo usuário.

    **Lógica:**
    - Utiliza um loop `while True` para garantir que o usuário digite uma operação válida.
    - Verifica se a operação está entre as opções permitidas (+, -, *, /).

    Returns:
        str: Operação escolhida pelo usuário.
    """
    while True:
        operacao = input("Digite a operação desejada (+, -, *, /): ")
        if operacao in ['+', '-', '*', '/']:
            return operacao
        else:
            print("Operação inválida. Por favor, escolha +, -, * ou /.")

def calculadora(numero1, numero2, operacao):
    """
    Realiza a operação matemática entre dois números.

    Args:
        numero1 (float): Primeiro número.
        numero2 (float): Segundo número.
        operacao (str): Operação matemática a ser realizada.

    Returns:
        float ou str: Resultado da operação ou mensagem de erro em caso de divisão por zero.
    """
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero não é permitida."

def main():
    """
    Função principal do programa.

    Solicita os números e a operação ao usuário, realiza o cálculo e exibe o resultado.
    """
    numero1 = solicitar_numero("Digite o primeiro número: ")
    numero2 = solicitar_numero("Digite o segundo número: ")
    operacao = solicitar_operacao()

    resultado = calculadora(numero1, numero2, operacao)
    print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()
