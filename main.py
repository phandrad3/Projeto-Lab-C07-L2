from dao.naveDAO import NaveDAO
from dao.pilotoDAO import PilotoDAO
from dao.missaoDAO import MissaoDAO
from dao.planetaDAO import PlanetaDAO
from dao.recursoDAO import RecursoDAO
from dao.consultaDAO import ConsultaDAO
from dao.missaoRealizadaDAO import MissaoRealizadaDAO
from dao.planetaHasRecursoDAO import PlanetaHasRecursoDAO

naveDao = NaveDAO()
piloto_dao = PilotoDAO()
missaoDAO = MissaoDAO()
planetaDAO = PlanetaDAO()
recursoDAO = RecursoDAO()
consultaDAO = ConsultaDAO()
missaoRealizadaDAO = MissaoRealizadaDAO()
planetaHasRecursoDAO = PlanetaHasRecursoDAO()

def main():
    menu_principal()

def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Gerenciar Naves")
        print("2 - Gerenciar Pilotos")
        print("3 - Gerenciar Missões")
        print("4 - Gerenciar Planetas")
        print("5 - Gerenciar Recursos")
        print("6 - Gerenciar Missões Realizadas") 
        print("7 - Gerenciar Recursos em Planetas") 
        print("8 - Realizar Consultas") 
        print("0 - Sair")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Encerrando o programa.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            break

        if opcao == "1":
            menu_nave(naveDao)
        elif opcao == "2":
            menu_piloto(piloto_dao)
        elif opcao == "3":
            menu_missao(missaoDAO)
        elif opcao == "4":
            menu_planeta(planetaDAO)
        elif opcao == "5":
            menu_recurso(recursoDAO)
        elif opcao == "6": 
            menu_missao_realizada(missaoRealizadaDAO)
        elif opcao == "7":  
            menu_planeta_has_recurso(planetaHasRecursoDAO)
        elif opcao == "8":
            menu_consultas(consultaDAO)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def menu_missao_realizada(dao):
    while True:
        print("\n--- Menu Missão Realizada ---")
        print("1 - Inserir Missão Realizada")
        print("2 - Atualizar Missão Realizada")
        print("3 - Deletar Missão Realizada")
        print("4 - Listar Missões Realizadas")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            planeta = input("Nome do Planeta: ")
            try:
                id_missao = int(input("ID da Missão: "))
            except ValueError:
                print("ID da Missão inválido! Deve ser um número inteiro.")
                continue
            problemas = input("Descrição dos problemas (opcional): ") or None
            dao.inserir(planeta, id_missao, problemas)

        elif opcao == "2":
            print("\n--- Missões Realizadas Registradas ---")
            missoes = dao.listar()
            if missoes:
                planeta = input("Nome do Planeta: ")
                try:
                    id_missao = int(input("ID da Missão: "))
                except ValueError:
                    print("ID da Missão inválido! Deve ser um número inteiro.")
                    continue
                problemas = input("Nova descrição dos problemas (opcional): ") or None
                dao.atualizar(planeta, id_missao, problemas)
            else:
                print("Nenhuma missão realizada registrada para atualizar.")

        elif opcao == "3":
            print("\n--- Missões Realizadas Registradas ---")
            missoes = dao.listar()
            if missoes:
                planeta = input("Nome do Planeta: ")
                try:
                    id_missao = int(input("ID da Missão: "))
                except ValueError:
                    print("ID da Missão inválido! Deve ser um número inteiro.")
                    continue
                dao.deletar(planeta, id_missao)
            else:
                print("Nenhuma missão realizada registrada para deletar.")

        elif opcao == "4":
            dao.listar()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_planeta_has_recurso(dao):
    while True:
        print("\n--- Menu Recursos em Planetas ---")
        print("1 - Inserir Recurso em Planeta")
        print("2 - Atualizar Recurso em Planeta")
        print("3 - Deletar Recurso em Planeta")
        print("4 - Listar Recursos em Planetas")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            planeta = input("Nome do Planeta: ")
            recurso = input("Nome do Recurso: ")
            quantidade_input = input("Quantidade (opcional): ") or None
            
            quantidade = None
            if quantidade_input is not None:
                try:
                    quantidade = float(quantidade_input)
                except ValueError:
                    print("Quantidade inválida! Deve ser um número.")
                    continue
            
            dao.inserir(planeta, recurso, quantidade)

        elif opcao == "2":
            print("\n--- Recursos em Planetas Registrados ---")
            recursos = dao.listar()
            if recursos:
                planeta = input("Nome do Planeta: ")
                recurso = input("Nome do Recurso: ")
                quantidade_input = input("Nova Quantidade (opcional): ") or None
                
                quantidade = None
                if quantidade_input is not None:
                    try:
                        quantidade = float(quantidade_input)
                    except ValueError:
                        print("Quantidade inválida! Deve ser um número.")
                        continue
                
                dao.atualizar(planeta, recurso, quantidade)
            else:
                print("Nenhum recurso em planeta registrado para atualizar.")

        elif opcao == "3":
            print("\n--- Recursos em Planetas Registrados ---")
            recursos = dao.listar()
            if recursos:
                planeta = input("Nome do Planeta: ")
                recurso = input("Nome do Recurso: ")
                dao.deletar(planeta, recurso)
            else:
                print("Nenhum recurso em planeta registrado para deletar.")

        elif opcao == "4":
            dao.listar()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_consultas(dao):
    while True:
        print("\n--- MENU DE CONSULTAS ---")
        print("1 - Consultas sem Tabelas Intermediárias")
        print("2 - Consultas com Tabelas Intermediárias")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            menu_consultas_sem_intermediarias(dao)
        elif opcao == "2":
            menu_consultas_com_intermediarias(dao)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_consultas_sem_intermediarias(dao):
    while True:
        print("\n--- CONSULTAS SEM TABELAS INTERMEDIÁRIAS ---")
        print("1 - Pilotos com suas Naves")
        print("2 - Missões com seus Pilotos")
        print("3 - Missões Realizadas")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu anterior.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu anterior.")
            break

        if opcao == "1":
            dao.pilotos_com_naves()
        elif opcao == "2":
            dao.missoes_com_pilotos()
        elif opcao == "3":
            dao.missoes_realizadas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_consultas_com_intermediarias(dao):
    while True:
        print("\n--- CONSULTAS COM TABELAS INTERMEDIÁRIAS ---")
        print("1 - Missões com Pilotos e Naves")
        print("2 - Recursos em Planetas Inóspitos")
        print("3 - Missões, Planetas e Recursos")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu anterior.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu anterior.")
            break

        if opcao == "1":
            dao.missao_piloto_nave()
        elif opcao == "2":
            dao.recursos_planetas_inospitos()
        elif opcao == "3":
            dao.missoes_planetas_recursos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_nave(dao):
    while True:
        print("\n--- Menu Nave ---")
        print("1 - Inserir Nave")
        print("2 - Atualizar Nave")
        print("3 - Deletar Nave")
        print("4 - Listar Naves")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            nome = input("Nome: ")
            try:
                capacidade = float(input("Capacidade: "))
            except ValueError:
                print("Capacidade inválida! Deve ser um número.")
                continue
            try:
                velocidade = float(input("Velocidade Máxima: "))
            except ValueError:
                print("Velocidade inválida! Deve ser um número.")
                continue
            dao.inserir(nome, capacidade, velocidade)

        elif opcao == "2":
            print("\n--- Naves Registradas ---")
            naves = dao.listar()
            if naves:
                try:
                    id_nave = int(input("ID da Nave que deseja atualizar: "))
                except ValueError:
                    print("ID inválido! Deve ser um número inteiro.")
                    continue

                nome = input("Novo Nome (vazio para não alterar): ") or None
                capacidade_input = input("Nova Capacidade (vazio para não alterar): ") or None
                velocidade_input = input("Nova Velocidade (vazio para não alterar): ") or None
                
                capacidade = None
                if capacidade_input is not None:
                    try:
                        capacidade = float(capacidade_input)
                    except ValueError:
                        print("Capacidade inválida! Deve ser um número.")
                        continue
                
                velocidade = None
                if velocidade_input is not None:
                    try:
                        velocidade = float(velocidade_input)
                    except ValueError:
                        print("Velocidade inválida! Deve ser um número.")
                        continue
                
                dao.atualizar(id_nave, nome, capacidade, velocidade)
            else:
                print("Nenhuma nave registrada para atualizar.")

        elif opcao == "3":
            print("\n--- Naves Registradas ---")
            naves = dao.listar()
            if naves:
                try:
                    id_nave = int(input("ID da Nave que deseja deletar: "))
                except ValueError:
                    print("ID inválido! Deve ser um número inteiro.")
                    continue
                dao.deletar(id_nave)
            else:
                print("Nenhuma nave registrada para deletar.")

        elif opcao == "4":
            dao.listar()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_piloto(dao):
    while True:
        print("\n--- Menu Piloto ---")
        print("1 - Inserir Piloto")
        print("2 - Atualizar Piloto")
        print("3 - Deletar Piloto")
        print("4 - Listar Pilotos")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            nome = input("Nome: ")
            try:
                nivel = int(input("Nível: "))
            except ValueError:
                print("Nível inválido! Deve ser um número inteiro.")
                continue
            try:
                id_nave = int(input("ID da Nave: "))
            except ValueError:
                print("ID da Nave inválido! Deve ser um número inteiro.")
                continue
            dao.inserir(nome, nivel, id_nave)

        elif opcao == "2":
            print("\n--- Pilotos Registrados ---")
            pilotos = dao.listar()
            if pilotos:
                try:
                    id_piloto = int(input("ID do Piloto que deseja atualizar: "))
                except ValueError:
                    print("ID inválido! Deve ser um número inteiro.")
                    continue

                nome = input("Novo Nome (vazio para não alterar): ") or None
                nivel_input = input("Novo Nível (vazio para não alterar): ") or None
                id_nave_input = input("Novo ID da Nave (vazio para não alterar): ") or None
                
                nivel = None
                if nivel_input is not None:
                    try:
                        nivel = int(nivel_input)
                    except ValueError:
                        print("Nível inválido! Deve ser um número inteiro.")
                        continue
                
                id_nave = None
                if id_nave_input is not None:
                    try:
                        id_nave = int(id_nave_input)
                    except ValueError:
                        print("ID da Nave inválido! Deve ser um número inteiro.")
                        continue
                
                dao.atualizar(id_piloto, nome, nivel, id_nave)
            else:
                print("Nenhum piloto registrado para atualizar.")

        elif opcao == "3":
            print("\n--- Pilotos Registrados ---")
            pilotos = dao.listar()
            if pilotos:
                try:
                    id_piloto = int(input("ID do Piloto que deseja deletar: "))
                except ValueError:
                    print("ID inválido! Deve ser um número inteiro.")
                    continue
                dao.deletar(id_piloto)
            else:
                print("Nenhum piloto registrado para deletar.")

        elif opcao == "4":
            dao.listar()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_missao(dao):
    while True:
        print("\n--- Menu Missão ---")
        print("1 - Inserir Missão")
        print("2 - Atualizar Missão")
        print("3 - Deletar Missão")
        print("4 - Listar Missões")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            nome = input("Nome: ")
            duracao = input("Duração (HH:MM:SS): ")
            status = input("Status (Planejada, Em Andamento, Concluída): ")
            try:
                id_piloto = int(input("ID do Piloto: "))
            except ValueError:
                print("ID do Piloto inválido! Deve ser um número inteiro.")
                continue
            dao.inserir(nome, duracao, status, id_piloto)

        elif opcao == "2":
            print("\n--- Missões Registradas ---")
            missoes = dao.listar()
            if missoes:
                try:
                    id_missao = int(input("ID da Missão que deseja atualizar: "))
                except ValueError:
                    print("ID inválido! Deve ser um número inteiro.")
                    continue

                nome = input("Novo Nome (vazio para não alterar): ") or None
                duracao = input("Nova Duração (vazio para não alterar): ") or None
                status = input("Novo Status (vazio para não alterar): ") or None
                id_piloto_input = input("Novo ID do Piloto (vazio para não alterar): ") or None
                
                id_piloto = None
                if id_piloto_input is not None:
                    try:
                        id_piloto = int(id_piloto_input)
                    except ValueError:
                        print("ID do Piloto inválido! Deve ser um número inteiro.")
                        continue
                
                dao.atualizar(id_missao, nome, duracao, status, id_piloto)
            else:
                print("Nenhuma missão registrada para atualizar.")

        elif opcao == "3":
            print("\n--- Missões Registradas ---")
            missoes = dao.listar()
            if missoes:
                try:
                    id_missao = int(input("ID da Missão que deseja deletar: "))
                except ValueError:
                    print("ID inválido! Deve ser um número inteiro.")
                    continue
                dao.deletar(id_missao)
            else:
                print("Nenhuma missão registrada para deletar.")

        elif opcao == "4":
            dao.listar()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_planeta(dao):
    while True:
        print("\n--- Menu Planeta ---")
        print("1 - Inserir Planeta")
        print("2 - Atualizar Planeta")
        print("3 - Deletar Planeta")
        print("4 - Listar Planetas")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            nome = input("Nome: ")
            tipo = input("Tipo (Gasoso, Aquático, Rochoso): ")
            try:
                habitavel = int(input("É habitável? (1 para Sim, 0 para Não): "))
                if habitavel not in [0, 1]:
                    print("Valor inválido! Deve ser 0 ou 1.")
                    continue
            except ValueError:
                print("Valor inválido! Deve ser 0 ou 1.")
                continue
            dao.inserir(nome, tipo, habitavel)

        elif opcao == "2":
            print("\n--- Planetas Registrados ---")
            planetas = dao.listar()
            if planetas:
                nome_planeta = input("Nome do Planeta que deseja atualizar: ")
                tipo = input("Novo Tipo (vazio para não alterar): ") or None
                habitavel_input = input("É habitável? (1 para Sim, 0 para Não, vazio para não alterar): ") or None
                
                habitavel = None
                if habitavel_input is not None:
                    try:
                        habitavel = int(habitavel_input)
                        if habitavel not in [0, 1]:
                            print("Valor inválido! Deve ser 0 ou 1.")
                            continue
                    except ValueError:
                        print("Valor inválido! Deve ser 0 ou 1.")
                        continue
                
                dao.atualizar(nome_planeta, tipo, habitavel)
            else:
                print("Nenhum planeta registrado para atualizar.")

        elif opcao == "3":
            print("\n--- Planetas Registrados ---")
            planetas = dao.listar()
            if planetas:
                nome_planeta = input("Nome do Planeta que deseja deletar: ")
                dao.deletar(nome_planeta)
            else:
                print("Nenhum planeta registrado para deletar.")

        elif opcao == "4":
            dao.listar()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_recurso(dao):
    while True:
        print("\n--- Menu Recurso ---")
        print("1 - Inserir Recurso")
        print("2 - Atualizar Recurso")
        print("3 - Deletar Recurso")
        print("4 - Listar Recursos")
        print("0 - Voltar")
        
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            print("\nErro de entrada. Voltando ao menu principal.")
            break
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal.")
            break

        if opcao == "1":
            nome = input("Nome: ")
            tipo = input("Tipo (Combustível, Gás, Minério, Alimento): ")
            try:
                valor = float(input("Valor Unitário: "))
            except ValueError:
                print("Valor inválido! Deve ser um número.")
                continue
            dao.inserir(nome, tipo, valor)

        elif opcao == "2":
            print("\n--- Recursos Registrados ---")
            recursos = dao.listar()
            if recursos:
                nome_recurso = input("Nome do Recurso que deseja atualizar: ")
                tipo = input("Novo Tipo (vazio para não alterar): ") or None
                valor_input = input("Novo Valor Unitário (vazio para não alterar): ") or None
                
                valor = None
                if valor_input is not None:
                    try:
                        valor = float(valor_input)
                    except ValueError:
                        print("Valor inválido! Deve ser um número.")
                        continue
                
                dao.atualizar(nome_recurso, tipo, valor)
            else:
                print("Nenhum recurso registrado para atualizar.")

        elif opcao == "3":
            print("\n--- Recursos Registrados ---")
            recursos = dao.listar()
            if recursos:
                nome_recurso = input("Nome do Recurso que deseja deletar: ")
                dao.deletar(nome_recurso)
            else:
                print("Nenhum recurso registrado para deletar.")

        elif opcao == "4":
            dao.listar()

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()