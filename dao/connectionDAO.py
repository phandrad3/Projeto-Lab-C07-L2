# connectionDAO.py
# Módulo responsável por estabelecer e gerenciar a conexão com o banco de dados MySQL.

import mysql.connector
from mysql.connector import Error

# Configurações do Banco de Dados
DB_CONFIG = {
    'host': 'localhost',
    'database': 'outerwilds',
    'user': 'comandante',
    'password': '1'
}

def get_connection():
    """Tenta estabelecer e retornar uma conexão com o MySQL."""
    print("Tentando conectar ao banco de dados...")
    try:
        # Tenta criar a conexão
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            print("Conexão estabelecida com sucesso!")
            return connection
        else:
            print("Erro ao conectar: Objeto de conexão inválido.")
            return None

    except Error as e:
        # Captura e exibe o erro em caso de falha na conexão
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def close_connection(connection, cursor=None):
    """Fecha o cursor e a conexão se estiverem ativos."""
    try:
        if cursor:
            cursor.close()
            # print("Cursor fechado.")
        if connection and connection.is_connected():
            connection.close()
            # print("Conexão MySQL fechada.")
    except Error as e:
        print(f"Erro ao fechar a conexão: {e}")

# Exemplo de uso para teste
if __name__ == '__main__':
    conn = get_connection()
    if conn:
        print(f"Status da conexão: {conn.is_connected()}")
        close_connection(conn)