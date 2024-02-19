from flask import request, jsonify
import psycopg2
from login_manager.login_manager import LoginManager
from database.database_connector import conectar_banco
 
def configure_get_sensor_data_route(app):
    login_manager = LoginManager(conectar_banco)
    
    @app.route('/get-sensor-data', methods=['GET'])
    def post_data():
        print("Requisição recebida")
        temperature = request.args.get('temperature')
        humidity = request.args.get('humidity')

        if temperature is not None and humidity is not None:
            try:
                temperature = float(temperature)
                humidity = float(humidity)

                cur = conectar_banco.cursor()
                cur.execute("INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)", (temperature, humidity))
                conectar_banco.commit()
                cur.close()

                return jsonify({'success': True}), 200
            except (ValueError, psycopg2.DatabaseError) as e:
                return jsonify({'error': 'Bad Request', 'message': str(e)}), 400
        else:
            return jsonify({'error': 'Missing data', 'message': 'Temperature and humidity required'}), 400