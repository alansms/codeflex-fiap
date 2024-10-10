import requests


def converter_temperatura(celsius, tipo="F"):
    """
    Função que converte uma temperatura de Celsius para Fahrenheit ou Kelvin.

    :param celsius: Valor da temperatura em graus Celsius.
    :param tipo: Unidade para conversão ("F" para Fahrenheit, "K" para Kelvin).
    :return: Temperatura convertida ou mensagem de erro se o tipo for inválido.
    """
    if tipo == "F":
        # Converte para Fahrenheit
        return (celsius * 9 / 5) + 32
    elif tipo == "K":
        # Converte para Kelvin
        return celsius + 273.15
    else:
        # Retorna mensagem de erro se o tipo for inválido
        return f"Erro: Tipo de conversão '{tipo}' não reconhecido. Use 'F' para Fahrenheit ou 'K' para Kelvin."


def obter_temperatura_online(cidade):
    """
    Função que obtém a temperatura atual de uma cidade usando a API WeatherAPI.

    :param cidade: Nome da cidade.
    :return: Temperatura em graus Celsius ou None em caso de erro.
    """
    api_key = "9d6f0b538c7b4d258af00742241010"  # Sua chave válida da WeatherAPI
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}&aqi=no"

    try:
        # Faz a requisição para a API
        resposta = requests.get(url)
        dados = resposta.json()

        # Verifica se a resposta contém dados de temperatura
        if resposta.status_code == 200:
            temperatura_celsius = dados['current']['temp_c']
            return temperatura_celsius
        else:
            print(f"Erro ao buscar dados de temperatura: {dados.get('error', {}).get('message', 'Erro desconhecido')}")
            return None
    except requests.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None


def main():
    """
    Função principal que obtém a temperatura online e aplica a conversão de temperatura.
    Permite reiniciar o processo ao final.
    """
    while True:
        cidade = input("Digite o nome da cidade para obter a temperatura atual: ")

        # Obter a temperatura online para a cidade
        temperatura_celsius = obter_temperatura_online(cidade)

        if temperatura_celsius is not None:
            print(f"\nA temperatura atual em {cidade} é: {temperatura_celsius:.2f}°C")

            # Solicita ao usuário o tipo de conversão desejada
            tipo = input("Deseja converter para Fahrenheit (F) ou Kelvin (K)? (Padrão: F): ").upper() or "F"

            # Converte a temperatura conforme a escolha do usuário
            temperatura_convertida = converter_temperatura(temperatura_celsius, tipo)

            if isinstance(temperatura_convertida, str):
                # Exibe a mensagem de erro caso o tipo seja inválido
                print(temperatura_convertida)
            else:
                unidade = "°F" if tipo == "F" else "K"
                print(f"A temperatura convertida é: {temperatura_convertida:.2f}{unidade}")
        else:
            print(f"Não foi possível obter a temperatura de {cidade}.")

        # Pergunta ao usuário se deseja reiniciar o processo
        reiniciar = input("\nDeseja consultar outra cidade? (s para sim, qualquer outra tecla para sair): ").lower()
        if reiniciar != 's':
            print("Programa encerrado.")
            break


# Chama a função principal
if __name__ == "__main__":
    main()