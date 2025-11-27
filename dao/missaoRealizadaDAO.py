from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class MissaoRealizadaDAO:
    def __init__(self):
        pass
    
    def inserir(self, planeta_nomePlaneta, missao_idMissao, problemas=None):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO Missao_Realizada (Planeta_nomePlaneta, Missao_idMissao, problemas) VALUES (%s, %s, %s)"
        data = (planeta_nomePlaneta, missao_idMissao, problemas)

        try:
            cursor.execute(query, data)
            conn.commit()
            print(f"\n[CREATE] Missão realizada no planeta {planeta_nomePlaneta} inserida com sucesso!")
            return True
        except Error as e:
            print(f"\n[CREATE] Erro ao inserir missão realizada: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def atualizar(self, planeta_nomePlaneta, missao_idMissao, problemas=None):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if problemas is not None:
            updates.append("problemas = %s")
            params.append(problemas)
        
        if not updates:
            print("\n[UPDATE] Nenhum campo para atualizar.")
            return False
        
        query = f"UPDATE Missao_Realizada SET {', '.join(updates)} WHERE Planeta_nomePlaneta = %s AND Missao_idMissao = %s"
        params.extend([planeta_nomePlaneta, missao_idMissao])

        try:
            cursor.execute(query, params)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[UPDATE] Missão realizada no planeta {planeta_nomePlaneta} atualizada com sucesso.")
                return True
            else:
                print(f"\n[UPDATE] Missão realizada no planeta {planeta_nomePlaneta} não encontrada para atualizar.")
                return False
        except Error as e:
            print(f"\n[UPDATE] Erro ao atualizar missão realizada: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def deletar(self, planeta_nomePlaneta, missao_idMissao):
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM Missao_Realizada WHERE Planeta_nomePlaneta = %s AND Missao_idMissao = %s"
        data = (planeta_nomePlaneta, missao_idMissao)

        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[DELETE] Missão realizada no planeta {planeta_nomePlaneta} deletada com sucesso.")
                return True
            else:
                print(f"\n[DELETE] Missão realizada no planeta {planeta_nomePlaneta} não encontrada para deletar.")
                return False
        except Error as e:
            print(f"\n[DELETE] Erro ao deletar missão realizada: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def listar(self):
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = "SELECT Planeta_nomePlaneta, Missao_idMissao, problemas FROM Missao_Realizada"

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[SELECT] Todas as Missões Realizadas:")
            if records:
                for row in records:
                    problema = row[2] if row[2] else "Nenhum problema reportado"
                    print(f"   Planeta: {row[0]}, ID Missão: {row[1]}, Problema: {problema}")
                return records
            else:
                print("   Nenhuma missão realizada encontrada.")
                return []
        except Error as e:
            print(f"\n[SELECT] Erro ao listar missões realizadas: {e}")
            return []
        finally:
            close_connection(conn, cursor)

