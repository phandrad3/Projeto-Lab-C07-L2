from dao.naveDAO import NaveDAO
from dao.pilotoDAO import PilotoDAO
from dao.missaoDAO import MissaoDAO
from dao.planetaDAO import PlanetaDAO
from dao.recursoDAO import RecursoDAO

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="ProjetoBD"
)

def menu():
    naveDao = NaveDAO()
    pilotoDao = PilotoDAO()
    missaoDao = MissaoDAO()
    plaentaDao = PlanetaDAO()
    recursoDao = RecursoDAO()
    
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Operações com Naves")
        print("2. Operações com Pilotos")
        print("3. Operações com Missões")
        print("4. Operações com Planetas")
        print("5. Operações com Recursos")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            menu_nave(naveDao)
        elif opcao == "2":
            menu_piloto(pilotoDao)
        elif opcao == "3":
            menu_missao(missaoDao)
        elif opcao == "4":
            menu_planeta(plaentaDao)
        elif opcao == "5":
            menu_recurso(recursoDao)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

def menu_nave(naveDao):
    while True:
        print("\n===== MENU DE NAVES =====")
        print("1. Inserir Nave")
        print("2. Atualizar Nave")
        print("3. Excluir Nave")
        print("4. Listar Naves")
        print("5. Buscar Nave por ID")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome da nave: ")
            capacidade = float(input("Capacidade: "))
            velocidade = float(input("Velocidade máxima: "))
            naveDao.insert(nome, capacidade, velocidade)
        elif opcao == "2":
            id_nave = int(input("ID da nave: "))
            print("Deixe em branco para não alterar")
            nome = input("Novo nome: ")
            capacidade = input("Nova capacidade: ")
            velocidade = input("Nova velocidade máxima: ")
            
            capacidade = float(capacidade) if capacidade else None
            velocidade = float(velocidade) if velocidade else None
            
            naveDao.update(id_nave, nome if nome else None, capacidade, velocidade)
        elif opcao == "3":
            id_nave = int(input("ID da nave: "))
            naveDao.delete(id_nave)
        elif opcao == "4":
            naveDao.select()
        elif opcao == "5":
            id_nave = int(input("ID da nave: "))
            naveDao.select(id_nave)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# Implementar menus similares para as outras entidades...

if __name__ == "__main__":
    menu()