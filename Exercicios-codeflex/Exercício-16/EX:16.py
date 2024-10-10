import requests


def celsius_para_fahrenheit(celsius):
    """
    Função que converte temperatura de Celsius para Fahrenheit.
    :param celsius: Temperatura em graus Celsius.
    :return: Temperatura convertida para Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def obter_dados_climaticos_online(cidade):
    """
    Função que obtém a temperatura atual e o horário de uma cidade usando a API WeatherAPI.
    :param cidade: Nome da cidade para qual se quer obter os dados.
    :return: Dicionário contendo a temperatura e o horário, ou None em caso de erro.
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
            horario_local = dados['location']['localtime']
            return {"temperatura": temperatura_celsius, "horario": horario_local}
        else:
            print(f"Erro ao buscar dados de temperatura: {dados.get('error', {}).get('message', 'Erro desconhecido')}")
            return None
    except requests.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None


def main():
    """
    Função principal que obtém a temperatura e o horário de São Paulo online,
    realiza a conversão para Fahrenheit e exibe os resultados.
    """
    cidade = "São Paulo"

    # Obter os dados climáticos online para São Paulo
    dados_climaticos = obter_dados_climaticos_online(cidade)

    if dados_climaticos is not None:
        temperatura_celsius = dados_climaticos["temperatura"]
        horario_local = dados_climaticos["horario"]

        # Chamar a função 'celsius_para_fahrenheit' para converter a temperatura
        temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

        # Exibir o resultado da conversão e o horário formatados
        print(
            f"A temperatura atual em {cidade} é {temperatura_celsius:.2f}°C, que corresponde a {temperatura_fahrenheit:.2f}°F.")
        print(f"O horário local é: {horario_local}")
    else:
        print(f"Não foi possível obter os dados de {cidade}.")


# Chama a função principal
if __name__ == "__main__":
    main()