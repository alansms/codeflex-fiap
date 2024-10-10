def contar_vogais(texto):
    """
    Função que conta as vogais em uma string, incluindo vogais acentuadas.
    Suporta maiúsculas e minúsculas.

    :param texto: String a ser analisada
    :return: Número de vogais na string
    """
    vogais = "aeiouáéíóúâêîôûãõAEIOUÁÉÍÓÚÂÊÎÔÛÃÕ"
    contador = sum(1 for letra in texto if letra in vogais)
    return contador


def vogal_mais_frequente(texto):
    """
    Função que identifica qual vogal aparece mais vezes na string.

    :param texto: String a ser analisada
    :return: A vogal mais frequente ou None se não houver vogais
    """
    vogais = "aeiouáéíóúâêîôûãõAEIOUÁÉÍÓÚÂÊÎÔÛÃÕ"
    frequencia = {vogal: 0 for vogal in vogais}

    for letra in texto:
        if letra in vogais:
            frequencia[letra] += 1

    vogal_mais_comum = max(frequencia, key=frequencia.get)

    return vogal_mais_comum if frequencia[vogal_mais_comum] > 0 else None


def questionario():
    """
    Função que faz um questionário com o usuário e coleta informações.
    :return: Uma única string com todas as respostas concatenadas.
    """
    print("Bem-vindo! Vamos fazer um breve questionário.\n")

    nome = input("Qual é o seu primeiro nome? ")
    sobrenome = input("Qual é o seu último sobrenome? ")
    nome_pet = input("Qual é o nome do seu pet? ")
    nome_mae = input("Qual é o nome da sua mãe? ")
    nome_pai = input("Qual é o nome do seu pai? ")
    cidade = input("Em qual cidade você nasceu? ")

    # Concatenar todas as respostas em uma única string
    respostas_concatenadas = f"{nome} {sobrenome} {nome_pet} {nome_mae} {nome_pai} {cidade}"

    return respostas_concatenadas


def main():
    """
    Função principal que faz o questionário e aplica as funções relacionadas às vogais.
    Permite o reinício do processo até o usuário decidir sair.
    """
    while True:
        # Faz o questionário e coleta as respostas
        respostas = questionario()

        # Contagem de vogais nas respostas
        quantidade_vogais = contar_vogais(respostas)
        vogal_frequente = vogal_mais_frequente(respostas)

        # Exibindo os resultados
        print(f"\nQuantidade total de vogais em suas respostas: {quantidade_vogais}")
        print(f"A vogal mais frequente em suas respostas é: {vogal_frequente}")

        # Pergunta ao usuário se ele quer reiniciar ou sair
        reiniciar = input("\nDeseja reiniciar o questionário? (s para sim, qualquer outra tecla para sair): ").lower()
        if reiniciar != 's':
            print("Programa encerrado.")
            break


# Chama a função principal
if __name__ == "__main__":
    main()