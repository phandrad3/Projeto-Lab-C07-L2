from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class NaveDAO:
    def __init__(self):
        pass
    
    def inserir(self, nome, capacidade, velocidadeMaxima):
        """Insere uma nova nave na tabela 'Nave'."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO Nave (nome, capacidade, velocidadeMaxima) VALUES (%s, %s, %s)"
        data = (nome, capacidade, velocidadeMaxima)

        try:
            cursor.execute(query, data)
            conn.commit()
            print(f"\n[CREATE] Nave {nome} inserida com sucesso! ID: {cursor.lastrowid}")
            return True
        except Error as e:
            print(f"\n[CREATE] Erro ao inserir nave: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def atualizar(self, idNave, nome=None, capacidade=None, velocidadeMaxima=None):
        """Atualiza dados de uma nave específica pelo ID."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if nome is not None:
            updates.append("nome = %s")
            params.append(nome)
        if capacidade is not None:
            updates.append("capacidade = %s")
            params.append(capacidade)
        if velocidadeMaxima is not None:
            updates.append("velocidadeMaxima = %s")
            params.append(velocidadeMaxima)
        
        if not updates:
            print("\n[UPDATE] Nenhum campo para atualizar.")
            return False
        
        query = f"UPDATE Nave SET {', '.join(updates)} WHERE idNave = %s"
        params.append(idNave)

        try:
            cursor.execute(query, params)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[UPDATE] Nave ID {idNave} atualizada com sucesso.")
                return True
            else:
                print(f"\n[UPDATE] Nenhuma nave encontrada com ID {idNave} para atualizar.")
                return False
        except Error as e:
            print(f"\n[UPDATE] Erro ao atualizar nave: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def deletar(self, idNave):
        """Deleta uma nave específica pelo ID."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM Nave WHERE idNave = %s"
        data = (idNave,)

        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[DELETE] Nave ID {idNave} deletada com sucesso.")
                return True
            else:
                print(f"\n[DELETE] Nenhuma nave encontrada com ID {idNave} para deletar.")
                return False
        except Error as e:
            print(f"\n[DELETE] Erro ao deletar nave: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def listar(self):
        """Lista todas as naves do banco de dados."""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = "SELECT idNave, nome, capacidade, velocidadeMaxima FROM Nave"

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[SELECT] Todas as Naves:")
            if records:
                for row in records:
                    print(f"   ID: {row[0]}, Nome: {row[1]}, Capacidade: {row[2]}, Velocidade: {row[3]}")
                return records
            else:
                print("   Nenhuma nave encontrada.")
                return []
        except Error as e:
            print(f"\n[SELECT] Erro ao listar naves: {e}")
            return []
        finally:
            close_connection(conn, cursor)

if __name__ == '__main__':
    # Teste da classe
    dao = NaveDAO()
    
    # INSERT
    dao.inserir("Nave Teste", 100.0, 5000.0)
    
    # SELECT ALL
    naves = dao.listar()
    
    if naves:
        # UPDATE
        dao.atualizar(naves[0][0], capacidade=150.0)
        
        # DELETE
        dao.deletar(naves[0][0])
    
    # SELECT ALL FINAL
    dao.listar()