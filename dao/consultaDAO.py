from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class ConsultaDAO:
    def __init__(self):
        pass
    
    def pilotos_com_naves(self):
        """Lista pilotos com suas naves"""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = """
        SELECT p.nome AS Piloto, n.nome AS Nave, n.velocidadeMaxima
        FROM Piloto p
        JOIN Nave n ON p.Nave_idNave = n.idNave
        """

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[READ] Pilotos e suas Naves:")
            if records:
                for row in records:
                    print(f"   Piloto: {row[0]}, Nave: {row[1]}, Velocidade: {row[2]}")
                return records
            else:
                print("   Nenhum registro encontrado.")
                return []
        except Error as e:
            print(f"\n[READ] Erro: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def missoes_com_pilotos(self):
        """Lista missões com seus pilotos"""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = """
        SELECT m.nome AS Missao, m.status, p.nome AS Piloto
        FROM Missao m
        JOIN Piloto p ON m.Piloto_idPiloto = p.idPiloto
        """

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[READ] Missões com Pilotos:")
            if records:
                for row in records:
                    print(f"   Missão: {row[0]}, Status: {row[1]}, Piloto: {row[2]}")
                return records
            else:
                print("   Nenhum registro encontrado.")
                return []
        except Error as e:
            print(f"\n[READ] Erro: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def missoes_realizadas(self):
        """Lista missões realizadas em planetas"""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = """
        SELECT m.nome AS Missao, mr.Planeta_nomePlaneta AS Planeta, mr.problemas
        FROM Missao m
        JOIN Missao_Realizada mr ON m.idMissao = mr.Missao_idMissao
        """

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[READ] Missões Realizadas:")
            if records:
                for row in records:
                    problema = row[2] if row[2] else "Nenhum problema reportado"
                    print(f"   Missão: {row[0]}, Planeta: {row[1]}, Problema: {problema}")
                return records
            else:
                print("   Nenhum registro encontrado.")
                return []
        except Error as e:
            print(f"\n[READ] Erro: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def missao_piloto_nave(self):
        """Lista missões com pilotos e naves"""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = """
        SELECT m.nome AS Missao, p.nome AS Piloto, n.nome AS Nave
        FROM Missao m
        JOIN Piloto p ON m.Piloto_idPiloto = p.idPiloto
        JOIN Nave n ON p.Nave_idNave = n.idNave
        """

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[READ] Missões com Pilotos e Naves:")
            if records:
                for row in records:
                    print(f"   Missão: {row[0]}, Piloto: {row[1]}, Nave: {row[2]}")
                return records
            else:
                print("   Nenhum registro encontrado.")
                return []
        except Error as e:
            print(f"\n[READ] Erro: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def recursos_planetas_inospitos(self):
        """Recursos em planetas inóspitos"""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = """
        SELECT 
            p.nomePlaneta AS Planeta,
            pr.Recurso_nomeRecurso AS Recurso,
            pr.quantidadeRecurso AS Quantidade
        FROM 
            Planeta p
        JOIN 
            Planeta_has_Recurso pr ON p.nomePlaneta = pr.Planeta_nomePlaneta
        WHERE 
            p.habitavel = 0
        """

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[READ] Recursos em Planetas Inóspitos:")
            if records:
                for row in records:
                    print(f"   Planeta: {row[0]}, Recurso: {row[1]}, Quantidade: {row[2]}")
                return records
            else:
                print("   Nenhum recurso encontrado em planetas inóspitos.")
                return []
        except Error as e:
            print(f"\n[READ] Erro: {e}")
            return []
        finally:
            close_connection(conn, cursor)

    def missoes_planetas_recursos(self):
        """Lista missões, planetas e recursos"""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = """
        SELECT 
            m.nome AS Missao,
            mr.Planeta_nomePlaneta AS Planeta,
            pr.Recurso_nomeRecurso AS Recurso,
            pr.quantidadeRecurso AS QuantidadeDisponivel
        FROM 
            Missao m
        JOIN 
            Missao_Realizada mr ON m.idMissao = mr.Missao_idMissao
        JOIN 
            Planeta_has_Recurso pr ON mr.Planeta_nomePlaneta = pr.Planeta_nomePlaneta
        ORDER BY 
            m.nome, mr.Planeta_nomePlaneta, pr.Recurso_nomeRecurso
        """

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[READ] Missões, Planetas e Recursos:")
            if records:
                for row in records:
                    print(f"   Missão: {row[0]}, Planeta: {row[1]}, Recurso: {row[2]}, Quantidade: {row[3]}")
                return records
            else:
                print("   Nenhum registro encontrado.")
                return []
        except Error as e:
            print(f"\n[READ] Erro: {e}")
            return []
        finally:
            close_connection(conn, cursor)

if __name__ == '__main__':
    dao = ConsultaDAO()
    
    dao.pilotos_com_naves()
    dao.missoes_com_pilotos()
    dao.missoes_realizadas()
    
    dao.missao_piloto_nave()
    dao.recursos_planetas()
    dao.missoes_planetas_recursos()