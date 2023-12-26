from flask import Flask, render_template, jsonify, request
import psycopg2

app = Flask(__name__)

parametros_conexao = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': '123'
}

def obter_conexao():
    return psycopg2.connect(**parametros_conexao)

def obter_dados():
    try:
        with obter_conexao() as connection, connection.cursor() as cursor:
            # Consulta SQL para obter todos os dados
            cursor.execute("SELECT data_hora, temperature, humidity FROM sensor_data")
            resultados = cursor.fetchall()

            # Transformar os resultados em listas para data_hora, temperatura e umidade
            timestamps = [result[0].strftime("%Y-%m-%d %H:%M:%S") for result in resultados]
            temperatura = [result[1] for result in resultados]
            umidade = [result[2] for result in resultados]

        return timestamps, temperatura, umidade

    except Exception as erro:
        # Registre o erro em um arquivo de log ou imprima no console
        print(f"Erro ao obter dados do banco de dados: {erro}")
        return [], [], []