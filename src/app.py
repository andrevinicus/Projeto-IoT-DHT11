import logging
from flask import Flask, Response, render_template, jsonify, request, redirect, url_for, session
from flask_cors import CORS
from auth_middleware.auth_middleware import AuthMiddleware
from historico_manager.historico_manager import HistoricoManager
from relatorios.relatorios import obter_dados
from user_manager.user_manager import UserManager
from login_manager.login_manager import LoginManager
import psycopg2

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)
app.secret_key = '123' # Troque para uma chave segura em um ambiente de produção

# Parâmetros de conexão
parametros_conexao = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': '123'
}



historico_manager = HistoricoManager(parametros_conexao)
login_manager = LoginManager(parametros_conexao)

# Configurar o middleware de autenticação
#AuthMiddleware(app, login_manager)

# Rota para a tela de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if login_manager.authenticate(username, password):
            session['username'] = username
            session['password'] = password
            return jsonify({'status': 'success', 'message': 'Login bem-sucedido'})
        else:
            return jsonify({'status': 'error', 'message': 'Usuário ou senha incorretos. Tente novamente.'})

    return render_template('login.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/index')
def index():
    return render_template('index.html')
# Rota para a tela de relatórios
@app.route('/relatorios')
def relatorios():
    try:
        timestamps, temperatura, umidade = obter_dados()  # Ajuste aqui
        return render_template('relatorios.html', timestamps=timestamps, temperatura=temperatura, umidade=umidade)

    except Exception as erro:
        logging.error(f"Erro ao obter dados para relatórios: {erro}")
        return jsonify({'error': 'Erro ao obter dados para relatórios'}), 500
@app.route('/get_reports', methods=['GET'])
def get_reports():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        # Chame a função para obter dados filtrados com base nas datas
        timestamps, temperatura, umidade = relatorios_instance.obter_dados_filtrados(start_date, end_date)

        return jsonify({'timestamps': timestamps, 'temperatura': temperatura, 'umidade': umidade})

    except Exception as erro:
        logging.error(f"Erro ao obter dados para relatórios: {erro}")
        return jsonify({'error': 'Erro ao obter dados para relatórios'}), 500

    
@app.route('/download', methods=['GET'])
def download():
    startdate = request.args.get('startdate')
    enddate = request.args.get('enddate')

    try:
        response = historico_manager.download_csv_period(startdate, enddate)

        if response:
            return response
        else:
            return jsonify({'error': 'Nenhum dado disponível para o período especificado'}), 404

    except Exception as erro:
        # Registre o erro em um arquivo de log
        print(f"Erro: {erro}")
        return jsonify({'error': 'Erro ao gerar arquivo CSV'}), 500

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        tipo_usuario_id = int(request.form.get('tipo_usuario'))  # Converta para inteiro

        if not username or not password or not email:
            return render_template('cadastro.html', info='Preencha todos os campos.')

        UserManager.adicionar_usuario(username, password, email)  # Remova o tipo_usuario_id desta linha
        return redirect(url_for('menu'))

    return render_template('cadastro.html', info=None)
@app.route('/get-sensor-data', methods=['GET'])
def post_data():
    print("Requisição recebida")
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity')

    if temperature is not None and humidity is not None:
        try:
            temperature = float(temperature)
            humidity = float(humidity)

            cur = parametros_conexao.cursor()
            cur.execute("INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)", (temperature, humidity))
            parametros_conexao.commit()
            cur.close()

            return jsonify({'success': True}), 200
        except (ValueError, psycopg2.DatabaseError) as e:
            return jsonify({'error': 'Bad Request', 'message': str(e)}), 400
    else:
        return jsonify({'error': 'Missing data', 'message': 'Temperature and humidity required'}), 400


# Rota para obter dados
@app.route('/data')
def get_data():
    historico_temperatura = []
    historico_umidade = []
    timestamps = []

    try:
        connection = psycopg2.connect(**parametros_conexao)
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

if __name__ == '__main__':
    app.run(debug=True)

