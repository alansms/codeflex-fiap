from pymongo import MongoClient  # Importando MongoClient para conectar-se a um servidor MongoDB
from pymongo.errors import ConnectionFailure, ConfigurationError, ServerSelectionTimeoutError

# Solicitar ao usuário o URI do servidor MongoDB
uri = input("Digite o URI do servidor MongoDB (ex: mongodb://localhost:27017/): ")

try:
    # Tentar conectar ao servidor MongoDB
    cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos

    # Verificar se a conexão foi bem-sucedida
    cliente.admin.command('ping')

    # Listar todos os bancos de dados disponíveis
    bancos_de_dados = cliente.list_database_names()

    # Exibir a lista de bancos de dados
    print("\nBancos de dados disponíveis:")
    for idx, banco in enumerate(bancos_de_dados):
        print(f"{idx + 1}. {banco}")

    # Solicitar ao usuário que selecione um banco de dados
    escolha = input("\nDigite o número do banco de dados que deseja selecionar: ")
    try:
        escolha_idx = int(escolha) - 1
        if 0 <= escolha_idx < len(bancos_de_dados):
            nome_banco_selecionado = bancos_de_dados[escolha_idx]
            banco_selecionado = cliente[nome_banco_selecionado]
            print(f"\nBanco de dados '{nome_banco_selecionado}' selecionado com sucesso.")

            # Listar coleções no banco de dados selecionado
            colecoes = banco_selecionado.list_collection_names()
            if colecoes:
                print(f"\nColeções no banco de dados '{nome_banco_selecionado}':")
                for colecao in colecoes:
                    print(f"\nColeção: {colecao}")
                    # Obter documentos da coleção
                    documentos = banco_selecionado[colecao].find()
                    documentos_lista = list(documentos)
                    if documentos_lista:
                        print("Documentos:")
                        for doc in documentos_lista:
                            print(doc)
                    else:
                        print("A coleção está vazia.")
            else:
                print("O banco de dados selecionado não possui coleções.")
        else:
            print("Opção inválida. Nenhum banco de dados selecionado.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

except (ConnectionFailure, ConfigurationError, ServerSelectionTimeoutError):
    print("\nNão foi possível conectar ao servidor MongoDB.")
    print("Verifique se o servidor está ativo e se o URI está correto.")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")

finally:
    # Fechar a conexão se ela foi estabelecida
    try:
        cliente.close()
    except:
        pass  # Se 'cliente' não foi definido, não faz nada
