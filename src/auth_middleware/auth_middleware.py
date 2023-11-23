# middlewares/auth_middleware.py
from flask import request, session, redirect, url_for

class AuthMiddleware:
    def __init__(self, app, login_manager):
        self.app = app
        self.login_manager = login_manager
        self.init_app()

    def init_app(self):
        self.app.before_request(self.before_request)

    def before_request(self):
        if self.app.endpoint and self.app.endpoint != 'login' and self.app.endpoint != 'cadastro':
            if 'username' not in session or not self.login_manager.authenticate(session['username'], session.get('password', '')):
                print(f"Usuário não autenticado. Redirecionando para a página de login. Endpoint: {request.endpoint}")
                return redirect(url_for('login'))
