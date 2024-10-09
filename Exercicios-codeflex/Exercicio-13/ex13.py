def solicitar_idade() -> int:
    """
    Solicita a idade do usuário.

    Retorna:
    int: Idade fornecida pelo usuário.
    """
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                return idade
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def classificar_idade(idade: int) -> str:
    """
    Classifica a pessoa em uma faixa etária baseada na idade fornecida.

    Parâmetros:
    idade (int): A idade da pessoa.

    Retorna:
    str: A classificação etária ("Criança", "Adolescente", "Adulto", "Idoso").
    """
    if idade < 12:
        return "Criança"
    elif 12 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 64:
        return "Adulto"
    else:
        return "Idoso"

if __name__ == "__main__":
    # Solicitar a idade do usuário
    idade = solicitar_idade()
    
    # Classificar a faixa etária
    classificacao = classificar_idade(idade)
    
    # Exibir a classificação etária
    print(f"Você é classificado como: {classificacao}")
