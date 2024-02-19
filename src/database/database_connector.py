# Altere o nome do módulo para evitar conflitos
# Nome do arquivo: database_connector.py

import psycopg2

def conectar_banco():
    parametros_conexao = {
        'host': 'localhost',
        'port': '5432',
        'database': 'postgres',
        'user': 'postgres',
        'password': '123'
    }

    try:
        connection = psycopg2.connect(**parametros_conexao)
        return connection
    except Exception as erro:
        # Registre o erro em um arquivo de log ou imprima para debug
        print(f"Erro na conexão com o banco de dados: {erro}")
        return None
