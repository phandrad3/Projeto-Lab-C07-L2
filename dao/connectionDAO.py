# connection_dao.py
# Módulo responsável por estabelecer e gerenciar a conexão com o banco de dados MySQL.

import mysql.connector
from mysql.connector import Error
from abc import ABC, abstractmethod

class ConnectionDAO(ABC):
    """
    Classe abstrata base para gerenciar conexões com o banco de dados MySQL.
    Implementa o padrão DAO para centralizar e reutilizar a lógica de conexão.
    """
    
    def __init__(self):
        """Inicializa as configurações do banco de dados."""
        self.host = "localhost"
        self.database = "outerwilds"
        self.user = "comandante"
        self.password = "1"
        self.connection = None
    
    def connect(self):
        """
        Estabelece uma conexão com o banco de dados MySQL.
        
        Returns:
            mysql.connector.connection.MySQLConnection: Objeto de conexão ativo ou None em caso de erro.
        """
        print("Tentando conectar ao banco de dados...")
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            
            if self.connection.is_connected():
                print("Conexão estabelecida com sucesso!")
                return self.connection
            else:
                print("Erro ao conectar: Objeto de conexão inválido.")
                return None
                
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None
    
    def disconnect(self):
        """Fecha a conexão com o banco de dados se estiver ativa."""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.close()
                print("Conexão MySQL fechada.")
        except Error as e:
            print(f"Erro ao fechar a conexão: {e}")
    
    def close_cursor(self, cursor):
        """
        Fecha o cursor se estiver ativo.
        
        Args:
            cursor: Objeto cursor do MySQL.
        """
        try:
            if cursor:
                cursor.close()
                # print("Cursor fechado.")
        except Error as e:
            print(f"Erro ao fechar o cursor: {e}")
    
    @abstractmethod
    def insert(self, entity):
        """Método abstrato para inserção de dados."""
        pass
    
    @abstractmethod
    def delete(self, id_value):
        """Método abstrato para exclusão de dados."""
        pass
    
    @abstractmethod
    def update(self, entity):
        """Método abstrato para atualização de dados."""
        pass
    
    @abstractmethod
    def select(self, id_value=None):
        """Método abstrato para seleção de dados."""
        pass

# Exemplo de uso para teste
if __name__ == '__main__':
    # Criar uma classe concreta para teste
    class TestDAO(ConnectionDAO):
        def insert(self, entity):
            print(f"Insert: {entity}")
        
        def delete(self, id_value):
            print(f"Delete: {id_value}")
        
        def update(self, entity):
            print(f"Update: {entity}")
        
        def select(self, id_value=None):
            print(f"Select: {id_value}")
    
    # Testar a conexão
    test_dao = TestDAO()
    conn = test_dao.connect()
    
    if conn:
        print(f"Status da conexão: {conn.is_connected()}")
        test_dao.disconnect()