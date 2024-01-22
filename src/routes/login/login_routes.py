from flask import render_template, request, jsonify, session, redirect, url_for
from login_manager.login_manager import LoginManager
from database.database import conexao_banco
def configure_login_route(app):
    login_manager = LoginManager(conexao_banco)

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
