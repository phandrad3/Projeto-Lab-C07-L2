from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class RecursoDAO:
    def __init__(self):
        pass
    
    def inserir(self, nomeRecurso, tipo, valorUnitario):
        """Insere um novo recurso na tabela 'Recurso'."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO Recurso (nomeRecurso, tipo, valorUnitario) VALUES (%s, %s, %s)"
        data = (nomeRecurso, tipo, valorUnitario)

        try:
            cursor.execute(query, data)
            conn.commit()
            print(f"\n[CREATE] Recurso {nomeRecurso} inserido com sucesso!")
            return True
        except Error as e:
            print(f"\n[CREATE] Erro ao inserir recurso: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def atualizar(self, nomeRecurso, tipo=None, valorUnitario=None):
        """Atualiza dados de um recurso específico pelo nome."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if tipo is not None:
            updates.append("tipo = %s")
            params.append(tipo)
        if valorUnitario is not None:
            updates.append("valorUnitario = %s")
            params.append(valorUnitario)
        
        if not updates:
            print("\n[UPDATE] Nenhum campo para atualizar.")
            return False
        
        query = f"UPDATE Recurso SET {', '.join(updates)} WHERE nomeRecurso = %s"
        params.append(nomeRecurso)

        try:
            cursor.execute(query, params)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[UPDATE] Recurso {nomeRecurso} atualizado com sucesso.")
                return True
            else:
                print(f"\n[UPDATE] Recurso {nomeRecurso} não encontrado para atualizar.")
                return False
        except Error as e:
            print(f"\n[UPDATE] Erro ao atualizar recurso: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def deletar(self, nomeRecurso):
        """Deleta um recurso específico pelo nome."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM Recurso WHERE nomeRecurso = %s"
        data = (nomeRecurso,)

        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[DELETE] Recurso {nomeRecurso} deletado com sucesso.")
                return True
            else:
                print(f"\n[DELETE] Recurso {nomeRecurso} não encontrado para deletar.")
                return False
        except Error as e:
            print(f"\n[DELETE] Erro ao deletar recurso: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def listar(self):
        """Lista todos os recursos do banco de dados."""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = "SELECT nomeRecurso, tipo, valorUnitario FROM Recurso"

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[SELECT] Todos os Recursos:")
            if records:
                for row in records:
                    print(f"   Nome: {row[0]}, Tipo: {row[1]}, Valor: {row[2]}")
                return records
            else:
                print("   Nenhum recurso encontrado.")
                return []
        except Error as e:
            print(f"\n[SELECT] Erro ao listar recursos: {e}")
            return []
        finally:
            close_connection(conn, cursor)

if __name__ == '__main__':
    # Teste da classe
    dao = RecursoDAO()
    
    # INSERT
    dao.inserir("Recurso Teste", "Minério", 100.0)
    
    # SELECT ALL
    recursos = dao.listar()
    
    if recursos:
        # UPDATE
        dao.atualizar(recursos[0][0], valorUnitario=150.0)
        
        # DELETE
        dao.deletar(recursos[0][0])
    
    # SELECT ALL FINAL
    dao.listar()