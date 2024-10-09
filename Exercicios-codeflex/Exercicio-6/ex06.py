import csv

# Função para ler e exibir o conteúdo do arquivo CSV
def ler_csv(caminho):
    try:
        with open(caminho, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            dados = list(leitor)
            for linha in dados:
                try:
                    print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}")
                except KeyError as e:
                    print(f"Erro: chave {e} não encontrada na linha {linha}")
            return dados
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        return None
    except PermissionError:
        print(f"Erro: sem permissão para ler o arquivo '{caminho}'.")
        return None
    except csv.Error as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None

# Função para atualizar a idade de uma pessoa
def atualizar_idade(dados, nome, nova_idade):
    try:
        for linha in dados:
            if linha['Nome'].lower() == nome.lower():
                linha['Idade'] = nova_idade
                print(f"Idade de {nome} atualizada para {nova_idade}.")
                return True
        print(f"Nome {nome} não encontrado.")
        return False
    except KeyError as e:
        print(f"Erro: chave {e} não encontrada.")
        return False
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar a idade: {e}")
        return False

# Função para salvar os dados atualizados de volta no CSV
def salvar_csv(caminho, dados):
    try:
        with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
            campos = ['Nome', 'Idade']
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(dados)
    except PermissionError:
        print(f"Erro: sem permissão para escrever no arquivo '{caminho}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

# Programa principal
if __name__ == "__main__":
    # Solicitando o nome do arquivo CSV
    caminho_csv = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")

    # Lendo o arquivo CSV e exibindo o conteúdo
    print("\nConteúdo do arquivo CSV:")
    dados_pessoas = ler_csv(caminho_csv)

    if dados_pessoas:
        # Solicitando o nome da pessoa e a nova idade
        nome_pessoa = input("\nDigite o nome da pessoa para atualizar a idade: ")
        nova_idade = input("Digite a nova idade: ")

        # Verificando se a nova idade é um número válido
        if not nova_idade.isdigit():
            print("Erro: a idade deve ser um número inteiro.")
        else:
            # Atualizando a idade
            if atualizar_idade(dados_pessoas, nome_pessoa, nova_idade):
                # Salvando as alterações de volta no arquivo CSV
                salvar_csv(caminho_csv, dados_pessoas)
                print("\nArquivo CSV atualizado com sucesso!")
            else:
                print("\nNenhuma alteração foi feita.")
    else:
        print("Não foi possível ler os dados do arquivo CSV.")
