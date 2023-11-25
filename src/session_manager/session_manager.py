from flask import session

class SessionManager:
    def __init__(self, app, admin_users, session_lifetime_seconds=900):
        self.app = app
        self.admin_users = admin_users
        self.session_lifetime_seconds = session_lifetime_seconds

        self.init_app()

    def init_app(self):
        self.app.before_request(self.before_request)

    def before_request(self):
        if 'username' in session and session['username'] not in self.admin_users:
            session.permanent = True

    def login_admin_user(self, username):
        if username in self.admin_users:
            session.permanent = False

    def logout_user(self):
        session.permanent = True