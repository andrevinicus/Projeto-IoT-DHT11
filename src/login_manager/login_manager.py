import psycopg2
import bcrypt
from psycopg2 import sql
from database.database_connector import conectar_banco


class LoginManager:
    def __init__(self, db_params):
        self.db_params = db_params

    def hash_password(self, password):
        # Gere um hash para a senha usando bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def authenticate(self, username, password):
        connection = None
        try:
            with psycopg2.connect(**self.db_params) as connection:
                with connection.cursor() as cursor:
                    # Consulta usando sql.SQL para evitar SQL injection
                    query = sql.SQL("SELECT {id}, {password} FROM usuarios WHERE {username} = {}").format(
                        id=sql.Identifier('username'),
                        password=sql.Identifier('password'),
                        username=sql.Placeholder()
                    )
                    cursor.execute(query, (username,))
                    result = cursor.fetchone()

                    if result:
                        # Verifique a senha usando bcrypt
                        stored_password = result[1]
                        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                            return True

            return False

        except Exception as error:
            print(f"Erro ao autenticar: {error}")
            return False
