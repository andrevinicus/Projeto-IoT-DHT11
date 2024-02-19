from flask import render_template, request, redirect, url_for
from login_manager.login_manager import LoginManager
from database.database_connector import conectar_banco
from user_manager.user_manager import UserManager

def configure_cadastro_route(app):
    login_manager = LoginManager(conectar_banco)
    
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
        