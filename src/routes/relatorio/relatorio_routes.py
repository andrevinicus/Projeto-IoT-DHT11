from flask import render_template, request, jsonify
from login_manager.login_manager import LoginManager
from database.database_connector import conectar_banco
from relatorios.relatorios import obter_dados
import logging

def configure_relatorio_route(app):
    login_manager = LoginManager(conectar_banco)   
    
    @app.route('/relatorios')
    def relatorios():
        try:
            timestamps, temperatura, umidade = obter_dados()  # Ajuste aqui
            return render_template('relatorios.html', timestamps=timestamps, temperatura=temperatura, umidade=umidade)

        except Exception as erro:
            logging.error(f"Erro ao obter dados para relatórios: {erro}")
            return jsonify({'error': 'Erro ao obter dados para relatórios'}), 500
    