from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class PlanetaHasRecursoDAO:
    def __init__(self):
        pass
    
    def inserir(self, planeta_nomePlaneta, recurso_nomeRecurso, quantidadeRecurso=None):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO Planeta_has_Recurso (Planeta_nomePlaneta, Recurso_nomeRecurso, quantidadeRecurso) VALUES (%s, %s, %s)"
        data = (planeta_nomePlaneta, recurso_nomeRecurso, quantidadeRecurso)

        try:
            cursor.execute(query, data)
            conn.commit()
            print(f"\n[CREATE] Recurso {recurso_nomeRecurso} no planeta {planeta_nomePlaneta} inserido com sucesso!")
            return True
        except Error as e:
            print(f"\n[CREATE] Erro ao inserir recurso no planeta: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def atualizar(self, planeta_nomePlaneta, recurso_nomeRecurso, quantidadeRecurso=None):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if quantidadeRecurso is not None:
            updates.append("quantidadeRecurso = %s")
            params.append(quantidadeRecurso)
        
        if not updates:
            print("\n[UPDATE] Nenhum campo para atualizar.")
            return False
        
        query = f"UPDATE Planeta_has_Recurso SET {', '.join(updates)} WHERE Planeta_nomePlaneta = %s AND Recurso_nomeRecurso = %s"
        params.extend([planeta_nomePlaneta, recurso_nomeRecurso])

        try:
            cursor.execute(query, params)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[UPDATE] Recurso {recurso_nomeRecurso} no planeta {planeta_nomePlaneta} atualizado com sucesso.")
                return True
            else:
                print(f"\n[UPDATE] Recurso {recurso_nomeRecurso} no planeta {planeta_nomePlaneta} não encontrado para atualizar.")
                return False
        except Error as e:
            print(f"\n[UPDATE] Erro ao atualizar recurso no planeta: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def deletar(self, planeta_nomePlaneta, recurso_nomeRecurso):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM Planeta_has_Recurso WHERE Planeta_nomePlaneta = %s AND Recurso_nomeRecurso = %s"
        data = (planeta_nomePlaneta, recurso_nomeRecurso)

        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[DELETE] Recurso {recurso_nomeRecurso} no planeta {planeta_nomePlaneta} deletado com sucesso.")
                return True
            else:
                print(f"\n[DELETE] Recurso {recurso_nomeRecurso} no planeta {planeta_nomePlaneta} não encontrado para deletar.")
                return False
        except Error as e:
            print(f"\n[DELETE] Erro ao deletar recurso no planeta: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def listar(self):
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = "SELECT Planeta_nomePlaneta, Recurso_nomeRecurso, quantidadeRecurso FROM Planeta_has_Recurso"

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[SELECT] Todos os Recursos em Planetas:")
            if records:
                for row in records:
                    quantidade = row[2] if row[2] is not None else "Não especificada"
                    print(f"   Planeta: {row[0]}, Recurso: {row[1]}, Quantidade: {quantidade}")
                return records
            else:
                print("   Nenhum recurso em planeta encontrado.")
                return []
        except Error as e:
            print(f"\n[SELECT] Erro ao listar recursos em planetas: {e}")
            return []
        finally:
            close_connection(conn, cursor)
