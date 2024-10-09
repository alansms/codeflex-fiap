# CodeFlex 💻

## Integrantes da equipe:
- **(CEO)** Alan de Souza Maximiano da Silva - RM557088
- **(Programador)** Lancelot Chagas Rodrigues - RM554707
- **(Revisor)** André Rovai Andrade Xavier Júnior - RM555848
- **(Documentador)** Renan de França Gonçalves - RM558413
  
## Descrição do Projeto:
Este repositório contém 20 exercícios em Python, abordando diferentes conceitos e estruturas de dados. Abaixo, você encontrará a descrição e a solução dos exercícios.

---

### EX:001 - Criação de uma Matriz 3x3

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-1/ex1.py)

```python
# Criando uma matriz 3x3, que é uma lista de listas, onde cada lista interna representa uma linha da matriz
matriz = [
    [1, 2, 3],  # Primeira linha da matriz
    [4, 5, 6],  # Segunda linha da matriz
    [7, 8, 9]   # Terceira linha da matriz
]

# Exibindo a matriz no console
# Para cada 'linha' na matriz, o laço percorre e imprime a linha inteira
for linha in matriz:
    print(linha)
```
---
### EX:002 - Multiplicação por Escalar

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-2/ex2.py)

```python
Crie uma matriz 2x2 e um número escalar. Multiplique cada elemento da matriz pelo escalar e exiba o resultado.

# Criando uma matriz 2x2, que é uma lista de listas, onde cada lista interna representa uma linha da matriz
matriz = [
    [2, 4],  # Primeira linha da matriz
    [6, 8]   # Segunda linha da matriz
]

# Definindo um número escalar que será usado para multiplicar cada elemento da matriz
escalar = 3

# Multiplicando cada elemento da matriz pelo escalar
# Para cada 'linha' na matriz, percorremos os 'elementos' e multiplicamos pelo valor do escalar
matriz_resultante = [[elemento * escalar for elemento in linha] for linha in matriz]

# Exibindo a matriz resultante no console
# Para cada linha da matriz resultante, imprimimos os valores multiplicados
for linha in matriz_resultante:
    print(linha)
```
---
---
### EX:003 - Leitura de Arquivo CSV

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-3/ex3.py)

```python
Crie um arquivo CSV com três colunas: Nome, Idade, Cidade. Depois, escreva um
programa em Python 

import csv  # Importando o módulo 'csv' que permite trabalhar com arquivos CSV (Comma Separated Values)

# Dados para o CSV
# Criamos uma lista de listas, onde cada lista interna representa uma linha a ser escrita no arquivo CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],  # Cabeçalho (primeira linha do arquivo)
    ['Alice', 25, 'São Paulo'],   # Linha com os dados de Alice
    ['Bruno', 30, 'Rio de Janeiro'],  # Linha com os dados de Bruno
    ['Carla', 22, 'Belo Horizonte']   # Linha com os dados de Carla
]

# Criando o arquivo CSV
# 'w' indica que o arquivo será aberto no modo de escrita (write)
# 'newline=""' evita a criação de linhas em branco extras ao escrever no arquivo
# 'encoding="utf-8"' garante que o arquivo seja gravado com a codificação UTF-8, suportando caracteres especiais
with open('dados.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)  # Criando o objeto 'escritor', que nos permite escrever no arquivo CSV
    escritor.writerows(dados)  # Escreve todas as linhas da lista 'dados' no arquivo de uma vez

# Mensagem de confirmação
print("Arquivo CSV 'dados.csv' criado com sucesso!")
```

---
### EX:004 - Conversão de JSON para Dicionário

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-4/ex4.py)

```python
Crie um arquivo JSON com informações de uma lista de produtos (nome, preço,
quantidade). Escreva um programa que leia esse arquivo e converta-o em um
dicionário Python.

import json  # Importando o módulo 'json', que permite trabalhar com arquivos no formato JSON (JavaScript Object Notation)

# Nome do arquivo JSON
arquivo_json = 'produtos.json'  # Definindo o nome do arquivo JSON que será lido

# Lendo o arquivo JSON
# 'r' indica que o arquivo será aberto no modo de leitura (read)
# 'encoding="utf-8"' garante que o arquivo seja lido com a codificação correta, suportando caracteres especiais
with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    produtos = json.load(arquivo)  # Carregando o conteúdo do arquivo JSON e convertendo para um dicionário Python

# Exibindo o dicionário Python resultante
print(produtos)  # Exibe o conteúdo do arquivo JSON, que agora está em formato de dicionário Python
```

---
### EX:005 - Escrita de Dados em Arquivo JSON

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-5/ex5.py)

[alunos.json](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-5/alunos.json)

```python
Crie um dicionário Python contendo dados de cinco alunos (nome, nota). Em
seguida, grave esse

import json  # Importando o módulo 'json', que permite trabalhar com arquivos no formato JSON (JavaScript Object Notation)

# Dicionário com dados de cinco alunos, contendo seus nomes e respectivas notas
dados_alunos = {
    "alunos": [
        {"nome": "João", "nota": 8.5},  # Dados do aluno João
        {"nome": "Maria", "nota": 9.0},  # Dados da aluna Maria
        {"nome": "Pedro", "nota": 7.0},  # Dados do aluno Pedro
        {"nome": "Ana", "nota": 8.0},    # Dados da aluna Ana
        {"nome": "Lucas", "nota": 6.5}   # Dados do aluno Lucas
    ]
}

# Caminho do arquivo JSON onde os dados dos alunos serão salvos
caminho_alunos_json = 'alunos.json'

# Gravando o dicionário 'dados_alunos' em um arquivo JSON
# 'w' indica que o arquivo será aberto no modo de escrita (write)
# 'encoding="utf-8"' garante que o arquivo seja gravado com a codificação UTF-8, suportando caracteres especiais
# 'ensure_ascii=False' garante que caracteres especiais (como acentos) sejam preservados
# 'indent=4' faz com que o JSON seja gravado de forma organizada (com identação)
with open(caminho_alunos_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_alunos, arquivo_json, ensure_ascii=False, indent=4)

# Mensagem de confirmação
print("Arquivo JSON 'alunos.json' criado com sucesso!")
```

---
### EX:006 - Atualização de Dados em CSV

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-6/ex6.py)

[pessoas.csv](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-6/pessoas%20(1).csv)

```python
Escreva um programa que leia um arquivo CSV com nomes e idades. Em seguida,
permita ao usuário atualizar a idade de uma pessoa e salve a alteração de volta
no arquivo CSV.

import csv  # Importa o módulo 'csv' para trabalhar com arquivos CSV (Comma Separated Values)

# Caminho do arquivo CSV
caminho_csv = 'pessoas.csv'  # Definindo o caminho e o nome do arquivo CSV que será lido e escrito

# Função para ler e exibir o conteúdo do arquivo CSV
def ler_csv(caminho):
    # Abre o arquivo CSV no modo de leitura ('r'), garantindo que a codificação seja UTF-8 e não adicionando novas linhas extras
    with open(caminho, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)  # Usa DictReader para ler o arquivo como um dicionário, com os títulos das colunas como chaves
        dados = list(leitor)  # Converte o conteúdo lido em uma lista de dicionários
        # Itera sobre cada linha (dicionário) e exibe o nome e idade das pessoas
        for linha in dados:
            print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}")
        return dados  # Retorna os dados lidos para serem utilizados em outras funções

# Função para atualizar a idade de uma pessoa no arquivo CSV
def atualizar_idade(dados, nome, nova_idade):
    # Itera sobre os dados para encontrar a pessoa pelo nome e atualizar a idade
    for linha in dados:
        # Compara os nomes ignorando letras maiúsculas e minúsculas
        if linha['Nome'].lower() == nome.lower():
            linha['Idade'] = nova_idade  # Atualiza a idade da pessoa
            print(f"Idade de {nome} atualizada para {nova_idade}.")  # Exibe mensagem de sucesso
            return True  # Retorna True se a pessoa foi encontrada e atualizada
    print(f"Nome {nome} não encontrado.")  # Mensagem caso o nome não seja encontrado
    return False  # Retorna False se o nome não for encontrado

# Função para salvar os dados atualizados de volta no arquivo CSV
def salvar_csv(caminho, dados):
    # Abre o arquivo CSV no modo de escrita ('w') para sobrescrever o conteúdo
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ['Nome', 'Idade']  # Define as colunas do arquivo (campo 'Nome' e campo 'Idade')
        escritor = csv.DictWriter(arquivo, fieldnames=campos)  # Cria um escritor CSV que escreverá dicionários com base nos campos definidos
        escritor.writeheader()  # Escreve a linha de cabeçalho (títulos das colunas)
        escritor.writerows(dados)  # Escreve todas as linhas de dados (já com as atualizações) no arquivo CSV

# Programa principal
if __name​⬤
```

---
### EX:007 - Conectar ao MongoDB

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-7/ex7.py)

```python
Escreva um programa em Python que se conecte a um banco de dados MongoDB
local e exiba uma lista dos bancos de dados disponíveis.

from pymongo import MongoClient  # Importando MongoClient, que permite conectar-se a um servidor MongoDB

# Conectar ao servidor MongoDB local
# O MongoClient cria uma conexão com o servidor MongoDB rodando no endereço 'localhost' (127.0.0.1) e na porta padrão 27017
cliente = MongoClient('mongodb://localhost:27017/')

# Listar todos os bancos de dados disponíveis no servidor MongoDB ao qual estamos conectados
bancos_de_dados = cliente.list_database_names()

# Exibir a lista de bancos de dados
print("Bancos de dados disponíveis:")
for banco in bancos_de_dados:  # Itera sobre cada banco de dados listado
    print(f"- {banco}")  # Exibe o nome de cada banco de dados encontrado

# Fechar a conexão
# Fecha a conexão com o servidor MongoDB, liberando recursos
cliente.close()
```

---
### EX:008 - Consulta de Documentos no MongoDB

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-8/ex8.py)

```python
Escreva um programa que consulte todos os documentos da coleção "alunos" no
MongoDB e exiba cada documento no console.

# Solicitar ao usuário um número inteiro
# A função 'input()' recebe a entrada do usuário como uma string, e a função 'int()' converte essa entrada para um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar
# O operador '%' (módulo) retorna o resto da divisão de 'numero' por 2
# Se o resto for 0, o número é par; caso contrário, é ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")  # Exibe uma mensagem indicando que o número é par
else:
    print(f"O número {numero} é ímpar.")  # Exibe uma mensagem indicando que o número é ímpar
```

---
### EX:009 - Exclusão de Documento no MongoDB

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-9/ex9.py)

```python
Escreva um programa que remova um documento da coleção "alunos" no
MongoDB, utilizando o nome do aluno como critério de exclusão.

from pymongo import MongoClient  # Importando MongoClient para se conectar e interagir com um banco de dados MongoDB

# Conectar ao servidor MongoDB local
# O MongoClient cria uma conexão com o servidor MongoDB rodando no localhost (127.0.0.1) na porta padrão 27017
cliente = MongoClient('mongodb://localhost:27017/')

# Acessar o banco de dados 'escola' e a coleção 'alunos'
# 'db' referencia o banco de dados 'escola', e 'colecao_alunos' referencia a coleção 'alunos' dentro desse banco
db = cliente['escola']
colecao_alunos = db['alunos']

# Solicitar o nome do aluno para exclusão
# O usuário digita o nome do aluno que será removido da coleção 'alunos'
nome_aluno = input("Digite o nome do aluno que deseja remover: ")

# Remover o documento com base no nome
# A função 'delete_one' remove o primeiro documento que corresponder ao critério especificado (neste caso, o nome do aluno)
resultado = colecao_alunos.delete_one({"nome": nome_aluno})

# Verificar se o documento foi removido
# 'resultado.deleted_count' retorna o número de documentos removidos; se for maior que 0, significa que o aluno foi removido com sucesso
if resultado.deleted_count > 0:
    print(f"O aluno '{nome_aluno}' foi removido com sucesso.")  # Exibe mensagem de sucesso
else:
    print(f"Nenhum aluno com o nome '{nome_aluno}' foi encontrado.")  # Exibe mensagem caso o nome não seja encontrado

# Fechar a conexão
# Fecha a conexão com o MongoDB para liberar os recursos
cliente.close()
```

---
### EX:010 - Consulta com Filtro

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-10/ex10.py)

```python
Desenvolva um programa que conecte ao MongoDB e faça uma consulta filtrada
para listar todos os clientes com idade superior a 30 anos.

from pymongo import MongoClient  # Importa o MongoClient para se conectar e interagir com o banco de dados MongoDB

# Conectar ao servidor MongoDB local
# O MongoClient cria uma conexão com o servidor MongoDB rodando no endereço 'localhost' (127.0.0.1) e na porta padrão 27017
mongo_client = MongoClient('mongodb://localhost:27017/')

# Acessar o banco de dados 'empresa' e a coleção 'clientes'
# A variável 'db' referencia o banco de dados chamado 'empresa', e 'colecao_clientes' referencia a coleção 'clientes' dentro deste banco
db = mongo_client['empresa']
colecao_clientes = db['clientes']

# Consultar todos os clientes com idade superior a 30 anos
# Utiliza-se o operador '$gt' (greater than) para selecionar documentos onde o campo 'idade' é maior que 30
clientes_acima_de_30 = colecao_clientes.find({"idade": {"$gt": 30}})

# Exibir os clientes encontrados
# O laço 'for' percorre o cursor retornado pela consulta e imprime o nome e a idade de cada cliente
print("Clientes com idade superior a 30 anos:")
for cliente in clientes_acima_de_30:
    print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}")  # Exibe o nome e a idade de cada cliente encontrado

# Fechar a conexão com o MongoDB
# A conexão com o MongoDB é fechada após a execução para liberar recursos
mongo_client.close()
```

---
### EX:011 - Verificar Número Par ou Ímpar

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-11/ex11.py)

```python
Escreva um programa que solicite ao usuário um número inteiro e utilize if e else
para verificar se o número é par ou ímpar. Exiba a mensagem correspondente.

# Solicitar ao usuário um número inteiro
# A função 'input()' recebe a entrada do usuário como uma string, e a função 'int()' converte essa entrada para um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar
# O operador '%' (módulo) retorna o resto da divisão de 'numero' por 2
# Se o resto for 0, o número é par; caso contrário, é ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")  # Exibe uma mensagem indicando que o número é par
else:
    print(f"O número {numero} é ímpar.")  # Exibe uma mensagem indicando que o número é ímpar
```

---
### EX:012 - Verificação de Maior Número

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-12/ex12.py)

```python
Crie um programa que peça ao usuário três números e use if, elif, e else para
determinar qual é o maior dos três. Exiba o maior número.

# Solicitar ao usuário três números
# As entradas são convertidas para o tipo float para permitir números decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determinar qual é o maior dos três números
# Verifica se o primeiro número é maior ou igual aos outros dois
if num1 >= num2 and num1 >= num3:
    maior = num1  # Se for, atribui o valor de 'num1' à variável 'maior'
# Se a primeira condição não for verdadeira, verifica se o segundo número é maior ou igual aos outros dois
elif num2 >= num1 and num2 >= num3:
    maior = num2  # Se for, atribui o valor de 'num2' à variável 'maior'
# Caso as duas condições anteriores não sejam verdadeiras, o terceiro número é o maior
else:
    maior = num3  # Atribui o valor de 'num3' à variável 'maior'

# Exibir o maior número
# Exibe o valor do maior número identificado
print(f"O maior número é: {maior}")
```

---
### EX:013 - Classificação de Idade

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-13/ex13.py)

```python
Escreva um programa que peça ao usuário sua idade e, utilizando if, elif, e else,
classifique a pessoa nas seguintes faixas etárias:
* Menor de 12 anos: "Criança"
* Entre 12 e 17 anos: "Adolescente"
* Entre 18 e 64 anos: "Adulto"
* 65 anos ou mais: "Idoso"

# Solicitar ao usuário sua idade
# A função 'input()' recebe a entrada do usuário como uma string, e a função 'int()' converte essa entrada para um número inteiro
idade = int(input("Digite sua idade: "))

# Classificar a pessoa na faixa etária correspondente
# Verifica se a idade é menor que 12, classificando como "Criança"
if idade < 12:
    classificacao = "Criança"
# Verifica se a idade está entre 12 e 17 (inclusive), classificando como "Adolescente"
elif 12 <= idade <= 17:
    classificacao = "Adolescente"
# Verifica se a idade está entre 18 e 64 (inclusive), classificando como "Adulto"
elif 18 <= idade <= 64:
    classificacao = "Adulto"
# Se a idade for maior que 64, classifica como "Idoso"
else:
    classificacao = "Idoso"

# Exibir a classificação etária
# Exibe a faixa etária correspondente à idade informada
print(f"Você é classificado como: {classificacao}")
```

---
### EX:014 - Sistema de Notas

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-14/ex14.py)

```python
Crie um programa que solicite ao usuário uma nota de 0 a 100 e utilize if, elif, e
else para imprimir a classificação correspondente:
* Nota >= 90: "A"
* Nota >= 80: "B"
* Nota >= 70: "C"
* Nota >= 60: "D"
* Nota < 60: "F"

# Solicitar ao usuário uma nota de 0 a 100
# A função 'input()' recebe a nota como uma string, e a função 'float()' converte para número decimal (float)
nota = float(input("Digite uma nota de 0 a 100: "))

# Classificar a nota de acordo com a escala
# Verifica se a nota é maior ou igual a 90 e atribui a classificação "A"
if nota >= 90:
    classificacao = "A"
# Verifica se a nota é maior ou igual a 80 e menor que 90, atribui a classificação "B"
elif nota >= 80:
    classificacao = "B"
# Verifica se a nota é maior ou igual a 70 e menor que 80, atribui a classificação "C"
elif nota >= 70:
    classificacao = "C"
# Verifica se a nota é maior ou igual a 60 e menor que 70, atribui a classificação "D"
elif nota >= 60:
    classificacao = "D"
# Se a nota for menor que 60, atribui a classificação "F"
else:
    classificacao = "F"

# Exibir a classificação correspondente
# Exibe a classificação da nota com base na escala definida
print(f"A classificação da nota é: {classificacao}")
```

---
### EX:015 - Calculadora Simples

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-15/ex15.py)

```python
Escreva um programa que solicite ao usuário dois números e uma operação
matemática (soma, subtração, multiplicação ou divisão). Use if, elif, e else para
realizar a operação correspondente e exibir o resultado.

# Solicitar ao usuário dois números
# O usuário digita dois números que são convertidos para o tipo float (permitindo números decimais)
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicitar ao usuário a operação matemática desejada
# O usuário insere um símbolo correspondente à operação: +, -, *, ou /
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realizar a operação com base na entrada do usuário
# Verifica qual operação foi selecionada e realiza o cálculo correspondente

if operacao == '+':
    # Se a operação for soma, soma os dois números
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
    
elif operacao == '-':
    # Se a operação for subtração, subtrai o segundo número do primeiro
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
    
elif operacao == '*':
    # Se a operação for multiplicação, multiplica os dois números
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
    
elif operacao == '/':
    # Se a operação for divisão, verifica primeiro se o divisor não é zero
    if numero2 != 0:
        resultado = numero1 / numero2  # Realiza a divisão
        print(f"O resultado da divisão é: {resultado}")
    else:
        # Exibe uma mensagem de erro se o divisor for zero, pois a divisão por zero não é permitida
        print("Erro: Divisão por zero não é permitida.")
        
else:
    # Caso o usuário tenha inserido um símbolo de operação inválido, exibe uma mensagem de erro
    print("Operação inválida. Por favor, escolha +, -, * ou /.")
```

---
### EX:016 - Função para Conversão de Temperatura

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-16/ex16.py)

```python
Escreva uma função chamada celsius_para_fahrenheit que receba uma
temperatura em graus Celsius como parâmetro e a converta para Fahrenheit.

# Definir a função que converte de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    # Fórmula de conversão de Celsius para Fahrenheit: (Celsius * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit  # Retorna a temperatura em Fahrenheit

# Exemplo de uso da função
# Solicitar ao usuário que insira a temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Chamar a função 'celsius_para_fahrenheit' passando a temperatura em Celsius como argumento
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# Exibir o resultado da conversão
print(f"{temperatura_celsius} graus Celsius é igual a {temperatura_fahrenheit} graus Fahrenheit.")
```

---
### EX:017 - Função para Calcular Média

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-17/ex17.py)

```python
Crie uma função chamada calcular_media que receba uma lista de números
como parâmetro e retorne a média desses números. Teste a função com
diferentes listas.

# Definir a função que calcula a média de uma lista de números
def calcular_media(numeros):
    # Verifica se a lista está vazia para evitar divisão por zero
    if len(numeros) == 0:
        return 0  # Retorna 0 se a lista estiver vazia
    # Calcula a média dos números
    # 'sum(numeros)' calcula a soma dos elementos da lista
    # 'len(numeros)' retorna a quantidade de elementos na lista
    media = sum(numeros) / len(numeros)
    return media  # Retorna a média calculada

# Testando a função com diferentes listas
lista1 = [10, 20, 30, 40, 50]  # Lista de inteiros
lista2 = [5, 7, 9, 11]  # Outra lista de inteiros
lista3 = [3.5, 7.2, 1.8, 9.9, 4.3]  # Lista de números decimais (float)
lista4 = []  # Lista vazia

# Exibindo a média de cada lista
print(f"Média de lista1: {calcular_media(lista1)}")  # Resultado: 30.0
print(f"Média de lista2: {calcular_media(lista2)}")  # Resultado: 8.0
print(f"Média de lista3: {calcular_media(lista3)}")  # Resultado: 5.34 (aproximadamente)
print(f"Média de lista4 (vazia): {calcular_media(lista4)}")  # Resultado: 0, pois a lista está vazia
```

---
### EX:018 - Função para Contar Vogais

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-18/ex18.py)

```python
Implemente uma função chamada contar_vogais que receba uma string como
parâmetro e retorne a quantidade de vogais presentes na string. Considere as
vogais "a", "e", "i", "o", "u" (maiúsculas e minúsculas).

# Definir a função que conta as vogais em uma string
def contar_vogais(texto):
    # Definindo as vogais tanto maiúsculas quanto minúsculas
    vogais = "aeiouAEIOU"
    # Contando quantas letras na string são vogais
    # A função 'sum()' soma 1 para cada letra que for encontrada na lista de vogais
    contador = sum(1 for letra in texto if letra in vogais)
    return contador  # Retorna o total de vogais encontradas

# Testando a função com diferentes strings
teste1 = "Olá, como vai você?"  # Teste com frase e acentuação
teste2 = "Python é incrível!"  # Teste com uma frase com vogais e acentuação
teste3 = "12345"  # Teste com números, sem vogais
teste4 = "AEIOU aeiou"  # Teste com vogais maiúsculas e minúsculas

# Exibir a quantidade de vogais em cada string
print(f"Quantidade de vogais em teste1: {contar_vogais(teste1)}")  # Resultado esperado: 7
print(f"Quantidade de vogais em teste2: {contar_vogais(teste2)}")  # Resultado esperado: 6
print(f"Quantidade de vogais em teste3: {contar_vogais(teste3)}")  # Resultado esperado: 0
print(f"Quantidade de vogais em teste4: {contar_vogais(teste4)}")  # Resultado esperado: 10
```

---
### EX:019 - Função para Encontrar o Máximo em uma Lista

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-19/ex19.py)

```python
Implemente uma função chamada encontrar_maximo que receba uma lista de
números como parâmetro e retorne o maior número da lista. Se a lista estiver
vazia, a função deve retornar None.

# Definir a função que encontra o maior número em uma lista
def encontrar_maximo(numeros):
    # Verifica se a lista está vazia
    # Se a lista estiver vazia, retorna 'None' para indicar que não há números
    if not numeros:
        return None
    # Usa a função 'max()' para encontrar o maior número da lista
    maximo = max(numeros)
    return maximo  # Retorna o maior número encontrado

# Testando a função com diferentes listas
lista1 = [10, 20, 30, 40, 50]  # Lista de inteiros positivos
lista2 = [5, -7, 9, -11]  # Lista com números positivos e negativos
lista3 = [3.5, 7.2, 1.8, 9.9, 4.3]  # Lista com números decimais (float)
lista4 = []  # Lista vazia

# Exibir o maior número de cada lista
print(f"Maior número em lista1: {encontrar_maximo(lista1)}")  # Resultado esperado: 50
print(f"Maior número em lista2: {encontrar_maximo(lista2)}")  # Resultado esperado: 9
print(f"Maior número em lista3: {encontrar_maximo(lista3)}")  # Resultado esperado: 9.9
print(f"Maior número em lista4 (vazia): {encontrar_maximo(lista4)}")  # Resultado esperado: None
```

---
### EX:020 - Função para Converter Temperatura

[Código fonte](https://github.com/alansms/codeflex-fiap/blob/main/Exercicios-codeflex/Exercicio-20/ex20.py)

```python
Crie uma função chamada converter_temperatura que receba um valor de
temperatura em Celsius e um parâmetro opcional chamado tipo, que pode ser
"F" (para Fahrenheit) ou "K" (para Kelvin). A função deve retornar a temperatura
convertida para a unidade especificada. Se tipo não for fornecido, retorne a
temperatura em Fahrenheit por padrão.

# Função que converte uma temperatura de Celsius para Fahrenheit ou Kelvin
def converter_temperatura(celsius, tipo="F"):
    # Converte para Fahrenheit se o tipo for "F" ou se não for especificado (valor padrão)
    if tipo == "F":
        return (celsius * 9/5) + 32
    # Converte para Kelvin se o tipo for "K"
    elif tipo == "K":
        return celsius + 273.15
    else:
        # Retorna None se um tipo inválido for fornecido
        return None

# Testando a função com diferentes valores e tipos
print(converter_temperatura(25))  # Padrão: converte para Fahrenheit, resultado esperado: 77.0
print(converter_temperatura(25, "F"))  # Converte para Fahrenheit, resultado esperado: 77.0
print(converter_temperatura(25, "K"))  # Converte para Kelvin, resultado esperado: 298.15
print(converter_temperatura(25, "X"))  # Tipo inválido, resultado esperado: None
```

## Como executar os códigos

1. **Certifique-se de ter o Python instalado em sua máquina.**
   - Caso não tenha, faça o download e instale o Python [aqui](https://www.python.org/downloads/).

2. **Clone este repositório para sua máquina local:**
   ```bash
   git clone https://github.com/CodeFlex/Exercicios-Python.git

3. **Navegue até o diretório do projeto:**
    ```bash
    cd Exercicios-Python

4. **Execute qualquer um dos exercícios com o seguinte comando:**
   ```bash
    python ex1.py
Substitua ex1.py pelo arquivo que deseja executar.
