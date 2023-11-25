import psycopg2

class LoginManager:
    def __init__(self, db_params):
        self.db_params = db_params

    def authenticate(self, username, password):
        try:
            connection = psycopg2.connect(**self.db_params)
            cursor = connection.cursor()

            # Consulta para verificar as credenciais na tabela "usuarios"
            query = "SELECT username, password FROM usuarios WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                return True
            else:
                return False

        except Exception as error:
            print(f"Erro ao autenticar: {error}")
            return False

        finally:
            if connection:
                cursor.close()
                connection.close()
