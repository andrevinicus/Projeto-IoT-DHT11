![GitHub language count](https://img.shields.io/github/languages/count/andrevinicus/Projeto-IoT-DHT11),![GitHub top language](https://img.shields.io/github/languages/top/andrevinicus/Projeto-IoT-DHT11?color=008000),


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
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/5f242313-b95d-46c7-bc4d-c04e28ae5778)

- Utiliza um middleware de autenticação (comentado no código).
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/87c1498a-ae7f-4ed9-944f-07e81e85a9ca)
- Tela de login
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/15e341f4-ff59-4da0-a237-07eaebe41c57)


### Página Inicial (/)

- Rota principal que exibe uma página HTML básica.

### Download de Dados (/download)

- Rota para baixar dados em formato CSV.
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/13928efb-ece8-40f0-a2cf-4019a08dd47d)

- Parâmetros: `startdate` e `enddate` para especificar o período.
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/e7b3729d-1749-4b07-8eec-b82633eed926)
  

### Cadastro de Usuário (/cadastro)

- Rota para cadastrar novos usuários.
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/80d872b3-084b-4fa0-bcb9-007cdc7690d9)

- Campos: username, password, email e tipo de usuário.
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/cfbed7d7-409a-4fa7-a7ea-27d8878fd028)


### Obtenção de Dados (/data)

- Rota que retorna dados de temperatura, umidade e timestamps dos últimos 10 registros.
  ![image](https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/3334dae7-0e1f-46e4-adc1-7e179c5318f3)

- Utiliza um banco de dados PostgreSQL.

## Utilização

1. Execute o arquivo `app.py` para iniciar o servidor Flask (`python app.py`).
2. Execute a API_Flask.py para fazer integraçâo com o Banco de Dados
3. Acesse a aplicação em um navegador (padrão: http://127.0.0.1:5000/login).
   
## Vidio de apresentaçao do software!
  

https://github.com/andrevinicus/Projeto-IoT-DHT11/assets/102330781/f2f02264-e370-4594-bda6-158bd546735a


## Membros do Grupo
- [André Vinicius (LinkedIn)](https://www.linkedin.com/in/andre-vinicius-gorlin-toledo-a797161b1/)
- [Mateus Stangherlin (LinkedIn)](https://www.linkedin.com/in/mateus-stangherlin-47a1b1230/)
- [Luiz Felipe Carli (GitHub)](https://github.com/felipeluizcarli)
- [André Vinicius (GitHub)](https://github.com/andrevinicus/Projeto-IoT-DHT11)
- [Ian Cadori de Siqueira(GitHub)](https://github.com/IanSiqueira)
- [Antonio Carlos Rodrigues Da Rosa(GitHub)](https://github.com/R-DaRosa-Antonio)

