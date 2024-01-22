from flask import render_template, request, jsonify, session, redirect, url_for
from login_manager.login_manager import LoginManager
from database.database import conexao_banco

def configure_menu_route(app):
    login_manager = LoginManager(conexao_banco)
    
    @app.route('/menu')
    def menu():
        return render_template('menu.html')