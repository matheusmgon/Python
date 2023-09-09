from os import getenv
from sys import exit
from Class.DatabaseConnect import DatabaseConnect


def check_env_var_exist(var_name):
    try:
        valor = getenv(var_name)
        return valor is not None
    except KeyError:
        return False


def main():
    env_vars = [
        "DB_NAME",
        "DB_PASSWORD",
        "DB_USER",
        "DB_HOST",
        "DB_PORT"
    ]

    if not all(check_env_var_exist(var) for var in env_vars):
        print("Algumas variáveis de ambiente não estão definidas.")
        return 1

    db = DatabaseConnect()
    if db.check_database_existence():
        print("O banco de dados já existe.")
        return 0
    else:
        print("O banco de dados não existe.")
        return 1


if __name__ == '__main__':
    exit(main())
