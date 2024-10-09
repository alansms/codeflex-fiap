def solicitar_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def solicitar_operacao():
    while True:
        operacao = input("Digite a operação desejada (+, -, *, /): ")
        if operacao in ['+', '-', '*', '/']:
            return operacao
        else:
            print("Operação inválida. Por favor, escolha +, -, * ou /.")

def calculadora(numero1, numero2, operacao):
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
    numero1 = solicitar_numero("Digite o primeiro número: ")
    numero2 = solicitar_numero("Digite o segundo número: ")
    operacao = solicitar_operacao()
    
    resultado = calculadora(numero1, numero2, operacao)
    print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()
