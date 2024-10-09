from pymongo import MongoClient  # Importa o MongoClient para se conectar e interagir com o banco de dados MongoDB
from pymongo.errors import ConnectionFailure, ConfigurationError, OperationFailure, ServerSelectionTimeoutError

try:
    # Solicitar ao usuário o URI do servidor MongoDB
    uri = input("Digite o URI do servidor MongoDB (ex: mongodb://localhost:27017/): ")

    # Conectar ao servidor MongoDB
    mongo_client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos

    # Verificar se a conexão foi bem-sucedida
    mongo_client.admin.command('ping')

    # Listar bancos de dados disponíveis
    bancos_de_dados = mongo_client.list_database_names()
    print("\nBancos de dados disponíveis:")
    for idx, banco in enumerate(bancos_de_dados):
        print(f"{idx + 1}. {banco}")

    # Solicitar ao usuário que selecione um banco de dados
    escolha_db = input("\nDigite o número do banco de dados que deseja selecionar: ")
    try:
        escolha_db_idx = int(escolha_db) - 1
        if 0 <= escolha_db_idx < len(bancos_de_dados):
            nome_banco_selecionado = bancos_de_dados[escolha_db_idx]
            db = mongo_client[nome_banco_selecionado]
            print(f"\nBanco de dados '{nome_banco_selecionado}' selecionado com sucesso.")
        else:
            print("Opção inválida. Nenhum banco de dados selecionado.")
            db = None
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        db = None

    if db is not None:
        # Solicitar o nome da coleção (opcional)
        nome_colecao = input("Digite o nome da coleção (padrão 'clientes'): ")
        if nome_colecao.strip() == "":
            nome_colecao = 'clientes'

        # Acessar a coleção especificada
        colecao_clientes = db[nome_colecao]

        # Solicitar a idade filtro
        idade_input = input("Digite a idade mínima dos clientes que deseja listar: ")
        try:
            idade_filtro = int(idade_input)
        except ValueError:
            print("Entrada inválida. A idade deve ser um número inteiro.")
            idade_filtro = None

        if idade_filtro is not None:
            # Consultar todos os clientes com idade superior à idade filtro
            clientes_filtrados = colecao_clientes.find({"idade": {"$gt": idade_filtro}})

            # Exibir os clientes encontrados
            print(f"\nClientes com idade superior a {idade_filtro} anos:")
            encontrados = False
            for cliente in clientes_filtrados:
                print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}")
                encontrados = True
            if not encontrados:
                print("Nenhum cliente encontrado com o critério especificado.")
        else:
            print("Não foi possível realizar a consulta devido à idade inválida.")
    else:
        print("Não foi possível prosseguir sem selecionar um banco de dados válido.")

except (ConnectionFailure, ConfigurationError, ServerSelectionTimeoutError):
    print("\nNão foi possível conectar ao servidor MongoDB.")
    print("Verifique se o servidor está ativo e se o URI está correto.")

except OperationFailure as e:
    print(f"\nOcorreu um erro na operação: {e}")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")

finally:
    # Fechar a conexão com o MongoDB
    try:
        mongo_client.close()
    except:
        pass  # Se 'mongo_client' não foi definido, não faz nada
