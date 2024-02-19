from flask import render_template, request, jsonify, session, redirect, url_for
from login_manager.login_manager import LoginManager
from database.database_connector import conectar_banco
 
def configure_index_route(app):
    login_manager = LoginManager(conectar_banco)
    @app.route('/index')
    def index():
        return render_template('index.html')