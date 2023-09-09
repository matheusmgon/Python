import psycopg2
from sys import exit
from os import getenv


class DatabaseConnect:
    def __init__(self):
        self.dbname = getenv('DB_NAME', default=None)
        self.dbuser = getenv('DB_USER', default=None)
        self.dbpassword = getenv('DB_PASSWORD', default=None)
        self.dbhost = getenv('DB_HOST', default=None)
        self.dbport = getenv('DB_PORT', default=None)

    def check_database_existence(self):
        try:
            # Estabelece uma conexão com o PostgreSQL
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.dbuser,
                password=self.dbpassword,
                host=self.dbhost,
                port=self.dbport
            )
            # Cria um cursor para executar consultas SQL
            cursor = conn.cursor()
            # Executa uma consulta para verificar se o banco de dados existe
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (self.dbname,))
            # Obtém o resultado da consulta
            result = cursor.fetchone()
            # Fecha a conexão
            conn.close()
            # Se o resultado não for vazio, o banco de dados existe
            if result:
                return True
            else:
                return False
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")
            return False
