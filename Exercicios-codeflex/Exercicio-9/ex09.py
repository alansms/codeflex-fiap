from pymongo import MongoClient  # Importando MongoClient para se conectar e interagir com um banco de dados MongoDB
from pymongo.errors import ConnectionFailure, ConfigurationError, OperationFailure

try:
    # Solicitar ao usuário o URI do servidor MongoDB
    uri = input("Digite o URI do servidor MongoDB (ex: mongodb://localhost:27017/): ")

    # Conectar ao servidor MongoDB
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos

    # Verificar se a conexão foi bem-sucedida
    cliente.admin.command('ping')

    # Listar bancos de dados disponíveis
    bancos_de_dados = cliente.list_database_names()
    print("\nBancos de dados disponíveis:")
    for idx, banco in enumerate(bancos_de_dados):
        print(f"{idx + 1}. {banco}")

    # Solicitar ao usuário que selecione um banco de dados
    escolha_db = input("\nDigite o número do banco de dados que deseja selecionar: ")
    try:
        escolha_db_idx = int(escolha_db) - 1
        if 0 <= escolha_db_idx < len(bancos_de_dados):
            nome_banco_selecionado = bancos_de_dados[escolha_db_idx]
            db = cliente[nome_banco_selecionado]
            print(f"\nBanco de dados '{nome_banco_selecionado}' selecionado com sucesso.")
        else:
            print("Opção inválida. Nenhum banco de dados selecionado.")
            db = None
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        db = None

    if db is not None:
        # Acessar a coleção 'alunos'
        colecao_alunos = db['alunos']

        # Solicitar o nome do aluno para exclusão
        nome_aluno = input("Digite o nome do aluno que deseja remover: ")

        # Remover o documento com base no nome
        resultado = colecao_alunos.delete_one({"nome": nome_aluno})

        # Verificar se o documento foi removido
        if resultado.deleted_count > 0:
            print(f"O aluno '{nome_aluno}' foi removido com sucesso.")
        else:
            print(f"Nenhum aluno com o nome '{nome_aluno}' foi encontrado.")
    else:
        print("Não foi possível prosseguir sem selecionar um banco de dados válido.")

except (ConnectionFailure, ConfigurationError):
    print("\nNão foi possível conectar ao servidor MongoDB.")
    print("Verifique se o servidor está ativo e se o URI está correto.")

except OperationFailure as e:
    print(f"\nOcorreu um erro na operação: {e}")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")

finally:
    # Fechar a conexão
    try:
        cliente.close()
    except:
        pass  # Se 'cliente' não foi definido, não faz nada
