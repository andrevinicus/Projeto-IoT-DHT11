from flask import render_template, request, jsonify, session, redirect, url_for
from historico_manager.historico_manager import HistoricoManager
from login_manager.login_manager import LoginManager
from database.database import conexao_banco


def configure_downloads_route(app):
    login_manager = LoginManager(conexao_banco)
    
    
    @app.route('/download', methods=['GET'])
    def download():
        startdate = request.args.get('startdate')
        enddate = request.args.get('enddate')

        try:
            response = HistoricoManager.download_csv_period(startdate, enddate)

            if response:
                return response
            else:
                return jsonify({'error': 'Nenhum dado disponível para o período especificado'}), 404

        except Exception as erro:
            # Registre o erro em um arquivo de log
            print(f"Erro: {erro}")
            return jsonify({'error': 'Erro ao gerar arquivo CSV'}), 500