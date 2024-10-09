from pymongo import MongoClient  # Importando MongoClient para conectar-se a um servidor MongoDB
from pymongo.errors import ConnectionFailure  # Importando exceção para erros de conexão

# Solicitar ao usuário o URI do servidor MongoDB
server_uri = input("Digite o URI do servidor MongoDB (ex: mongodb://localhost:27017/): ")

try:
    # Conectar ao servidor MongoDB usando o URI fornecido pelo usuário
    cliente = MongoClient(server_uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 segundos

    # Tentar uma operação simples para verificar a conexão
    cliente.admin.command('ping')

    # Listar todos os bancos de dados disponíveis
    bancos_de_dados = cliente.list_database_names()

    # Exibir a lista de bancos de dados
    print("\nBancos de dados disponíveis:")
    for banco in bancos_de_dados:
        print(f"- {banco}")

except ConnectionFailure:
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
