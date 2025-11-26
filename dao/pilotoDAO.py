from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class PilotoDAO:
    def __init__(self):
        pass
    
    def inserir(self, nome, nivel, Nave_idNave):
        """Insere um novo piloto na tabela 'Piloto'."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO Piloto (nome, nivel, Nave_idNave) VALUES (%s, %s, %s)"
        data = (nome, nivel, Nave_idNave)

        try:
            cursor.execute(query, data)
            conn.commit()
            print(f"\n[CREATE] Piloto {nome} inserido com sucesso! ID: {cursor.lastrowid}")
            return True
        except Error as e:
            print(f"\n[CREATE] Erro ao inserir piloto: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def atualizar(self, idPiloto, nome=None, nivel=None, Nave_idNave=None):
        """Atualiza dados de um piloto específico pelo ID."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if nome is not None:
            updates.append("nome = %s")
            params.append(nome)
        if nivel is not None:
            updates.append("nivel = %s")
            params.append(nivel)
        if Nave_idNave is not None:
            updates.append("Nave_idNave = %s")
            params.append(Nave_idNave)
        
        if not updates:
            print("\n[UPDATE] Nenhum campo para atualizar.")
            return False
        
        query = f"UPDATE Piloto SET {', '.join(updates)} WHERE idPiloto = %s"
        params.append(idPiloto)

        try:
            cursor.execute(query, params)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[UPDATE] Piloto ID {idPiloto} atualizado com sucesso.")
                return True
            else:
                print(f"\n[UPDATE] Nenhum piloto encontrado com ID {idPiloto} para atualizar.")
                return False
        except Error as e:
            print(f"\n[UPDATE] Erro ao atualizar piloto: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def deletar(self, idPiloto):
        """Deleta um piloto específico pelo ID."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM Piloto WHERE idPiloto = %s"
        data = (idPiloto,)

        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[DELETE] Piloto ID {idPiloto} deletado com sucesso.")
                return True
            else:
                print(f"\n[DELETE] Nenhum piloto encontrado com ID {idPiloto} para deletar.")
                return False
        except Error as e:
            print(f"\n[DELETE] Erro ao deletar piloto: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def listar(self):
        """Lista todos os pilotos do banco de dados."""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = "SELECT idPiloto, nome, nivel, Nave_idNave FROM Piloto"

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[SELECT] Todos os Pilotos:")
            if records:
                for row in records:
                    print(f"   ID: {row[0]}, Nome: {row[1]}, Nível: {row[2]}, Nave: {row[3]}")
                return records
            else:
                print("   Nenhum piloto encontrado.")
                return []
        except Error as e:
            print(f"\n[SELECT] Erro ao listar pilotos: {e}")
            return []
        finally:
            close_connection(conn, cursor)

if __name__ == '__main__':
    # Teste da classe
    dao = PilotoDAO()
    
    # INSERT
    dao.inserir("Piloto Teste", 5, 1)
    
    # SELECT ALL
    pilotos = dao.listar()
    
    if pilotos:
        # UPDATE
        dao.atualizar(pilotos[0][0], nivel=10)
        
        # DELETE
        dao.deletar(pilotos[0][0])
    
    # SELECT ALL FINAL
    dao.listar()