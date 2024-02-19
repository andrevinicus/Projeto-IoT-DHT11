from flask import app, render_template, request, jsonify, session, redirect, url_for
from login_manager.login_manager import LoginManager
from database.database_connector import conectar_banco

def configure_menu_route(app):
    login_manager = LoginManager(conectar_banco)
    
    @app.route('/menu')
    def menu():
        return render_template('menu.html')