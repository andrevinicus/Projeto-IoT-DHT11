import psycopg2

class UserManager:
    parametros_conexao = {
        'host': 'localhost',
        'port': '5432',
        'database': 'postgres',
        'user': 'postgres',
        'password': '123'
    }

    @classmethod
    def adicionar_usuario(cls, username, password, email):
        try:
            with psycopg2.connect(**cls.parametros_conexao) as connection, connection.cursor() as cursor:
                query = "INSERT INTO usuarios (username, password, email) VALUES (%s, %s, %s)"
                cursor.execute(query, (username, password, email))
                connection.commit()

        except (Exception, psycopg2.Error) as erro:
            print(f"Erro ao adicionar usuário ao banco de dados: {erro}")

    @classmethod
    def criar_tabela(cls):
        try:
            with psycopg2.connect(**cls.parametros_conexao) as connection, connection.cursor() as cursor:
                query = """
                CREATE TABLE IF NOT EXISTS usuarios (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL
                )
                """
                cursor.execute(query)
                connection.commit()

        except (Exception, psycopg2.Error) as erro:
            print(f"Erro ao criar a tabela de usuários: {erro}")

# Agora, crie a tabela de usuários ao iniciar o aplicativo
UserManager.criar_tabela()
