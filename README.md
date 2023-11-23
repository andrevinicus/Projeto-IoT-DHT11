![GitHub language count](https://img.shields.io/github/languages/count/andrevinicus/Projeto-IoT-DHT11),![GitHub top language](https://img.shields.io/github/languages/top/andrevinicus/Projeto-IoT-DHT11)


# Projeto Flask com ESP32 - Monitoramento de Dados de Sensores

Este projeto utiliza Flask para criar uma aplicação web que permite o monitoramento e download de dados de sensores. A aplicação se conecta a um banco de dados PostgreSQL para recuperar e exibir informações sobre temperatura e umidade. Além disso, oferece funcionalidades de login, cadastro e download de dados em formato CSV.

## Tecnologias Utilizadas

- **Flask**: Framework web utilizado para criar a aplicação.
- **PostgreSQL**: Banco de dados relacional para armazenar os dados dos sensores.
- **psycopg2**: Adaptador PostgreSQL para Python.

## Requisitos

- Python 3.x
- Flask (`pip install flask`)
- PostgreSQL

## Configuração

1. Configure o banco de dados PostgreSQL com os parâmetros fornecidos no código.
2. Instale as dependências do Flask usando o comando `pip install flask`.

## Funcionalidades

### Página de Login (/login)

- Rota para realizar login na aplicação.
- Utiliza um middleware de autenticação (comentado no código).

### Página Inicial (/)

- Rota principal que exibe uma página HTML básica.

### Download de Dados (/download)

- Rota para baixar dados em formato CSV.
- Parâmetros: `startdate` e `enddate` para especificar o período.

### Cadastro de Usuário (/cadastro)

- Rota para cadastrar novos usuários.
- Campos: username, password, email e tipo de usuário.

### Obtenção de Dados (/data)

- Rota que retorna dados de temperatura, umidade e timestamps dos últimos 10 registros.
- Utiliza um banco de dados PostgreSQL.

## Utilização

1. Execute o arquivo `app.py` para iniciar o servidor Flask (`python app.py`).
2. Acesse a aplicação em um navegador (padrão: http://127.0.0.1:5000/).


## Membros do Grupo

- [Mateus Stangherlin (LinkedIn)](https://www.linkedin.com/in/mateus-stangherlin-47a1b1230/)
- [Luiz Felipe Carli (GitHub)](https://github.com/felipeluizcarli)
- [André Vinicius (GitHub)](https://github.com/andrevinicus/Projeto-IoT-DHT11)

