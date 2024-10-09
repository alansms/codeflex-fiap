def verificar_paridade(numero: int) -> str:
    """
    Verifica se o número é par ou ímpar.

    Parâmetros:
    numero (int): O número inteiro a ser verificado.

    Retorna:
    str: Mensagem indicando se o número é par ou ímpar.
    """
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."

def solicitar_numero() -> int:
    """
    Solicita um número inteiro ao usuário.

    Retorna:
    int: O número inteiro fornecido pelo usuário.
    """
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    numero = solicitar_numero()
    mensagem = verificar_paridade(numero)
    print(mensagem)
