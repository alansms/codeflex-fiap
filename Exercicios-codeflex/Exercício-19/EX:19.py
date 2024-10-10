def encontrar_maximo(numeros):
    """
    Função que encontra o maior número em uma lista.
    Se a lista estiver vazia ou não houver números válidos, retorna None.

    :param numeros: Lista de números
    :return: Maior número da lista ou None se a lista estiver vazia
    """
    # Verifica se a lista está vazia
    if not numeros:
        return None

    # Filtra apenas os valores numéricos da lista
    numeros_validos = [num for num in numeros if isinstance(num, (int, float))]

    # Se não houver números válidos na lista, retorna None
    if not numeros_validos:
        return None

    # Usa a função 'max()' para encontrar o maior número da lista filtrada
    maximo = max(numeros_validos)
    return maximo


def questionario_para_numeros():
    """
    Função que solicita ao usuário que insira números e preenche uma lista.
    Ignora valores não numéricos.

    :return: Lista de números válidos preenchida pelo usuário.
    """
    numeros = []
    print("Por favor, insira números. Digite 'sair' para encerrar o questionário.\n")

    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")

        if entrada.lower() == 'sair':
            break

        # Tenta converter a entrada para número
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

    return numeros


def main():
    """
    Função principal que preenche uma lista de números com um questionário e
    encontra o maior número.
    """
    # Inicialmente, a lista está vazia
    lista_numeros = []

    # Preenche a lista de números com o questionário
    lista_numeros = questionario_para_numeros()

    # Verifica o maior número da lista
    maior_numero = encontrar_maximo(lista_numeros)

    # Exibindo o resultado
    if maior_numero is not None:
        print(f"\nO maior número da lista é: {maior_numero}")
    else:
        print("\nNenhum número válido foi inserido.")


# Chama a função principal
if __name__ == "__main__":
    main()