from flask import render_template, request, jsonify, session, redirect, url_for
import psycopg2
from login_manager.login_manager import LoginManager
from database.database import conexao_banco

def configure_data_route(app):
    login_manager = LoginManager(conexao_banco)
    
    @app.route('/data')
    def get_data():
        historico_temperatura = []
        historico_umidade = []
        timestamps = []

        try:
            connection = psycopg2.connect(**conexao_banco)
            cursor = connection.cursor()

            # Exemplo de consulta para obter os últimos 10 registros com data e hora
            cursor.execute("SELECT temperature, humidity, data_hora FROM public.sensor_data ORDER BY id DESC LIMIT 10")
            resultados = cursor.fetchall()

            # Transformar os resultados em listas para temperatura, umidade e timestamps
            for resultado in resultados:
                temperature, humidity, data_hora = resultado
                historico_temperatura.append(int(temperature))
                historico_umidade.append(int(humidity))
                timestamps.append(data_hora.strftime("%Y-%m-%d %H:%M:%S"))

            return jsonify({'temperature': historico_temperatura, 'humidity': historico_umidade, 'timestamps': timestamps})

        except Exception as erro:
            # Registre o erro em um arquivo de log
            print(f"Erro: {erro}")
            return jsonify({'error': 'Erro ao obter dados'}), 500

        finally:
            # Fechar a conexão
            if connection:
                cursor.close()
                connection.close()