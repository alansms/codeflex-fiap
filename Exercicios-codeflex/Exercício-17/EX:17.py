import logging
# EX:017 - Função para Calcular Média
# Configuração básica do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calcular_media(numeros):
    """
    Função que calcula a média de uma lista de números.
    Ignora elementos que não são numéricos e gera um log informativo.
    """
    lista_filtrada = [num for num in numeros if isinstance(num, (int, float))]

    if not lista_filtrada:
        logging.warning("A lista está vazia ou não contém valores numéricos válidos.")
        return 0

    media = sum(lista_filtrada) / len(lista_filtrada)
    logging.info(f"Números válidos considerados: {lista_filtrada}")
    return media


def obter_entrada_usuario():
    """
    Função que solicita ao usuário para inserir números e retorna uma lista deles.
    """
    print("Este programa calcula a média de uma lista de números inseridos por você.")
    print("Por favor, insira uma lista de números separados por espaço.")

    entrada = input("Insira os números: ")

    # Convertendo a entrada em uma lista de números, ignorando entradas inválidas
    numeros = []
    for item in entrada.split():
        try:
            numeros.append(float(item))  # Tenta converter cada entrada para float
        except ValueError:
            logging.warning(f"Valor inválido ignorado: {item}")

    return numeros


def main():
    """
    Função principal que mantém o programa em execução até o usuário decidir sair.
    """
    while True:
        numeros_usuario = obter_entrada_usuario()
        media = calcular_media(numeros_usuario)
        print(f"A média dos números inseridos é: {media}")

        # Pergunta ao usuário se ele quer continuar ou sair
        continuar = input("Pressione 's' para sair ou qualquer outra tecla para calcular novamente: ").lower()
        if continuar == 's':
            print("Programa encerrado.")
            break


# Chama a função principal
main()