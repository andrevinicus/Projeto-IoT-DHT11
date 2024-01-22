from flask import Flask
from flask_cors import CORS
from auth_middleware.auth_middleware import AuthMiddleware
from historico_manager.historico_manager import HistoricoManager
from routes.cadastro.cadastro_routes import configure_cadastro_route
from login_manager.login_manager import LoginManager
from database.database import conexao_banco
from routes.data.data_routes import configure_data_route
from routes.login.login_routes import configure_login_route
from routes.menu.menu_routes import configure_menu_route
from routes.index.index_routes import configure_index_route
from routes.relatorio.relatorio_routes import configure_relatorio_route
from routes.downloads.downloads_routes import configure_downloads_route
from routes.get_sensor_data.get_sensor_data import configure_get_sensor_data_route

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)
app.secret_key = '123'

historico_manager = HistoricoManager(conexao_banco)
login_manager = LoginManager(conexao_banco)

# Configurar o middleware de autenticação
#AuthMiddleware(app, login_manager)

configure_login_route(app) 
configure_menu_route(app)   
configure_index_route(app)
configure_relatorio_route(app)
configure_downloads_route(app)
configure_cadastro_route(app)
configure_get_sensor_data_route(app)
configure_data_route(app)

if __name__ == '__main__':
    app.run(debug=True)

