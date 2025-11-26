from .connectionDAO import get_connection, close_connection
from mysql.connector import Error

class MissaoDAO:
    def __init__(self):
        pass
    
    def inserir(self, nome, duracao, status, Piloto_idPiloto):
        """Insere uma nova missão na tabela 'Missao'."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO Missao (nome, duracao, status, Piloto_idPiloto) VALUES (%s, %s, %s, %s)"
        data = (nome, duracao, status, Piloto_idPiloto)

        try:
            cursor.execute(query, data)
            conn.commit()
            print(f"\n[CREATE] Missão {nome} inserida com sucesso! ID: {cursor.lastrowid}")
            return True
        except Error as e:
            print(f"\n[CREATE] Erro ao inserir missão: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def atualizar(self, idMissao, nome=None, duracao=None, status=None, Piloto_idPiloto=None):
        """Atualiza dados de uma missão específica pelo ID."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if nome is not None:
            updates.append("nome = %s")
            params.append(nome)
        if duracao is not None:
            updates.append("duracao = %s")
            params.append(duracao)
        if status is not None:
            updates.append("status = %s")
            params.append(status)
        if Piloto_idPiloto is not None:
            updates.append("Piloto_idPiloto = %s")
            params.append(Piloto_idPiloto)
        
        if not updates:
            print("\n[UPDATE] Nenhum campo para atualizar.")
            return False
        
        query = f"UPDATE Missao SET {', '.join(updates)} WHERE idMissao = %s"
        params.append(idMissao)

        try:
            cursor.execute(query, params)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[UPDATE] Missão ID {idMissao} atualizada com sucesso.")
                return True
            else:
                print(f"\n[UPDATE] Nenhuma missão encontrada com ID {idMissao} para atualizar.")
                return False
        except Error as e:
            print(f"\n[UPDATE] Erro ao atualizar missão: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def deletar(self, idMissao):
        """Deleta uma missão específica pelo ID."""
        conn = get_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = "DELETE FROM Missao WHERE idMissao = %s"
        data = (idMissao,)

        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[DELETE] Missão ID {idMissao} deletada com sucesso.")
                return True
            else:
                print(f"\n[DELETE] Nenhuma missão encontrada com ID {idMissao} para deletar.")
                return False
        except Error as e:
            print(f"\n[DELETE] Erro ao deletar missão: {e}")
            conn.rollback()
            return False
        finally:
            close_connection(conn, cursor)
    
    def listar(self):
        """Lista todas as missões do banco de dados."""
        conn = get_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = "SELECT idMissao, nome, duracao, status, Piloto_idPiloto FROM Missao"

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            print("\n[SELECT] Todas as Missões:")
            if records:
                for row in records:
                    print(f"   ID: {row[0]}, Nome: {row[1]}, Duração: {row[2]}, Status: {row[3]}, Piloto: {row[4]}")
                return records
            else:
                print("   Nenhuma missão encontrada.")
                return []
        except Error as e:
            print(f"\n[SELECT] Erro ao listar missões: {e}")
            return []
        finally:
            close_connection(conn, cursor)

if __name__ == '__main__':
    # Teste da classe
    dao = MissaoDAO()
    
    # INSERT
    dao.inserir("Missão Teste", "02:30:00", "Planejada", 1)
    
    # SELECT ALL
    missoes = dao.listar()
    
    if missoes:
        # UPDATE
        dao.atualizar(missoes[0][0], status="Em Andamento")
        
        # DELETE
        dao.deletar(missoes[0][0])
    
    # SELECT ALL FINAL
    dao.listar()