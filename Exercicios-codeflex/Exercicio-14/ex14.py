def solicitar_nota() -> float:
    """
    Solicita ao usuário uma nota entre 0 e 100.

    Retorna:
    float: A nota fornecida pelo usuário.
    """
    while True:
        try:
            nota = float(input("Digite uma nota de 0 a 100: "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("A nota deve estar entre 0 e 100. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def classificar_nota(nota: float) -> str:
    """
    Classifica a nota de acordo com a escala de A a F.

    Parâmetros:
    nota (float): A nota a ser classificada.

    Retorna:
    str: A classificação da nota (A, B, C, D, F).
    """
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    # Solicitar a nota do usuário
    nota = solicitar_nota()
    
    # Classificar a nota
    classificacao = classificar_nota(nota)
    
    # Exibir a classificação correspondente
    print(f"A classificação da nota é: {classificacao}")
