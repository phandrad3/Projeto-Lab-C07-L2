from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class PlanetaDAO:
    def __init__(self):
        pass
    
    def inserir(self, nomePlaneta, tipo, habitavel):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO Planeta (nomePlaneta, tipo, habitavel) VALUES (%s, %s, %s)"
        data = (nomePlaneta, tipo, habitavel)

        try:
            cursor.execute(query, data)
            conn.commit()
            print(f"\n[CREATE] Planeta {nomePlaneta} inserido com sucesso!")
            return True
        except Error as e:
            print(f"\n[CREATE] Erro ao inserir planeta: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def atualizar(self, nomePlaneta, tipo=None, habitavel=None):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if tipo is not None:
            updates.append("tipo = %s")
            params.append(tipo)
        if habitavel is not None:
            updates.append("habitavel = %s")
            params.append(habitavel)
        
        if not updates:
            print("\n[UPDATE] Nenhum campo para atualizar.")
            return False
        
        query = f"UPDATE Planeta SET {', '.join(updates)} WHERE nomePlaneta = %s"
        params.append(nomePlaneta)

        try:
            cursor.execute(query, params)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[UPDATE] Planeta {nomePlaneta} atualizado com sucesso.")
                return True
            else:
                print(f"\n[UPDATE] Planeta {nomePlaneta} não encontrado para atualizar.")
                return False
        except Error as e:
            print(f"\n[UPDATE] Erro ao atualizar planeta: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def deletar(self, nomePlaneta):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM Planeta WHERE nomePlaneta = %s"
        data = (nomePlaneta,)

        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[DELETE] Planeta {nomePlaneta} deletado com sucesso.")
                return True
            else:
                print(f"\n[DELETE] Planeta {nomePlaneta} não encontrado para deletar.")
                return False
        except Error as e:
            print(f"\n[DELETE] Erro ao deletar planeta: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def listar(self):
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = "SELECT nomePlaneta, tipo, habitavel FROM Planeta"

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[SELECT] Todos os Planetas:")
            if records:
                for row in records:
                    print(f"   Nome: {row[0]}, Tipo: {row[1]}, Habitável: {'Sim' if row[2] else 'Não'}")
                return records
            else:
                print("   Nenhum planeta encontrado.")
                return []
        except Error as e:
            print(f"\n[SELECT] Erro ao listar planetas: {e}")
            return []
        finally:
            close_connection(conn, cursor)
