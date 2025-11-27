DROP DATABASE IF EXISTS outerwilds;
CREATE DATABASE outerwilds;
USE outerwilds;

SET SQL_SAFE_UPDATES = 0;



-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Usuario =-=-=-=-=-=-=-=-=-=-=-=-=-=
DROP USER IF EXISTS 'comandante'@'localhost';
CREATE USER 'comandante'@'localhost' IDENTIFIED BY '1';
GRANT ALL PRIVILEGES ON outerwilds.* TO 'comandante'@'localhost';

SELECT * FROM mysql.user;
SHOW GRANTS FOR 'comandante'@'localhost';
-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Usuario =-=-=-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Tabelas =-=-=-=-=-=-=-=-=-=-=-=-=-=
CREATE TABLE Nave(
    idNave INT AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    capacidade FLOAT NOT NULL,
    velocidadeMaxima FLOAT NOT NULL,
    
    PRIMARY KEY(idNave)
);

CREATE TABLE Recurso(
    nomeRecurso VARCHAR(45),
    tipo ENUM("Combustível", "Gás", "Minério", "Alimento") NOT NULL,
    valorUnitario FLOAT NOT NULL,
    
    PRIMARY KEY(nomeRecurso)
);

CREATE TABLE Planeta(
    nomePlaneta VARCHAR(45),
    tipo ENUM("Gasoso", "Aquático", "Rochoso") NOT NULL,
    habitavel TINYINT(1),
    
    PRIMARY KEY(nomePlaneta)
);

CREATE TABLE Piloto(
    idPiloto INT AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    nivel INT NOT NULL,
    Nave_idNave	INT NOT NULL,
    
    PRIMARY KEY(idPiloto),
    
    CONSTRAINT fk_Piloto_Nave
    FOREIGN KEY(Nave_idNave) REFERENCES Nave(idNave) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Missao(
    idMissao INT AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    duracao TIME,
    status ENUM("Planejada", "Em Andamento", "Concluída") NOT NULL,
    Piloto_idPiloto INT NOT NULL,
    
    PRIMARY KEY(idMissao),
    
    CONSTRAINT fk_Missao_Piloto 
    FOREIGN KEY(Piloto_idPiloto) REFERENCES Piloto(idPiloto) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Missao_Realizada(
    Planeta_nomePlaneta VARCHAR(45) NOT NULL,
    Missao_idMissao INT NOT NULL,
    problemas VARCHAR(200),

    PRIMARY KEY(Planeta_nomePlaneta, Missao_idMissao),
    
    CONSTRAINT fk_MissaoRealizada_Planeta 
    FOREIGN KEY(Planeta_nomePlaneta) REFERENCES Planeta(nomePlaneta) ON DELETE CASCADE ON UPDATE CASCADE,
    
    CONSTRAINT fk_MissaoRealizada_Missao
    FOREIGN KEY(Missao_idMissao) REFERENCES Missao(idMissao) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Planeta_has_Recurso(
    Planeta_nomePlaneta VARCHAR(45) NOT NULL,
    Recurso_nomeRecurso VARCHAR(45) NOT NULL,
    quantidadeRecurso FLOAT,

    PRIMARY KEY(Planeta_nomePlaneta, Recurso_nomeRecurso),
    
    CONSTRAINT fk_PlanetaRecurso_Planeta
    FOREIGN KEY(Planeta_nomePlaneta) REFERENCES Planeta(nomePlaneta) ON DELETE CASCADE ON UPDATE CASCADE,
    
    CONSTRAINT fk_PlanetaRecurso_Recursomissao 
    FOREIGN KEY(Recurso_nomeRecurso) REFERENCES Recurso(nomeRecurso) ON DELETE CASCADE ON UPDATE CASCADE
);
-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Tabelas =-=-=-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Inserts =-=-=-=-=-=-=-=-=-=-=-=-=-=
INSERT INTO Nave VALUES
    (1, "Nave do Felsdpar", 120, 10000),
    (2, "Nave do Pack", 150, 11500),
    (3, "Nave do Seborreia", 200, 9000);

INSERT INTO Piloto VALUES
    (1, "Felsdpar", 1, 1),
    (2, "Pack", 1, 2),
    (3, "Seborreia", 1, 3);

INSERT INTO Missao VALUES
    (1, "Investigar o Projeto Gêmeo Cinzento", "02:30:00", "Concluída", 1),
    (2, "Investigar o Olho do Universo", "04:00:00", "Em Andamento", 2),
    (3, "Investigar sobre a Lua Quântica", "01:45:00", "Planejada", 3);

INSERT INTO Planeta VALUES
    ("Gêmeo Cinzento", "Rochoso", 1),
    ("Abrolho Sombrio", "Rochoso", 0),
    ("Profundezas do Gigante", "Aquático", 0);

INSERT INTO Recurso VALUES
    ("Combustível Nomai", "Combustível", 500.0),
    ("Cristais Quânticos", "Minério", 250.0),
    ("Ração Espacial", "Alimento", 50.0);

INSERT INTO Planeta_has_Recurso VALUES
    ("Gêmeo Cinzento", "Ração Espacial", 150.0),
    ("Abrolho Sombrio", "Combustível Nomai", 75.0),
    ("Profundezas do Gigante", "Cristais Quânticos", 200.0);

INSERT INTO Missao_Realizada VALUES
    ("Gêmeo Cinzento", 1, "Anomalia detectada no observatório."),
    ("Abrolho Sombrio", 2, "Perda de comunicação temporária com o piloto. Estrutura planetária instável."),
    ("Profundezas do Gigante", 3, "Tempestades elétricas impediram análise completa da superfície.");
    
SELECT * FROM Nave;
SELECT * FROM Piloto;
SELECT * FROM Missao;
SELECT * FROM Planeta;
SELECT * FROM Recurso;
SELECT * FROM Planeta_has_Recurso;
SELECT * FROM Missao_Realizada;
-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Inserts =-=-=-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-=-=-=  View  =-=-=-=-=-=-=-=-=-=-=-=-=-=
CREATE VIEW Recursos_em_Planetas_Inospitos AS
SELECT 
    p.nomePlaneta AS Planeta,
    pr.Recurso_nomeRecurso AS Recurso,
    pr.quantidadeRecurso AS Quantidade
FROM 
    Planeta p
JOIN 
    Planeta_has_Recurso pr ON p.nomePlaneta = pr.Planeta_nomePlaneta
WHERE 
    p.habitavel = 0;
    
SELECT * FROM Recursos_em_Planetas_Inospitos;
-- =-=-=-=-=-=-=-=-=-=-=-=-=-=  View  =-=-=-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-= Procedure =-=-=-=-=-=-=-=-=-=-=-=
DELIMITER $$
 
CREATE PROCEDURE Realizar_Missao(
    IN p_planeta_nome VARCHAR(45),
    IN p_missao_id INT,
    IN p_problemas VARCHAR(200)
)

BEGIN
    INSERT INTO Missao_Realizada(Planeta_nomePlaneta, Missao_idMissao, problemas)
    VALUES (p_planeta_nome, p_missao_id, p_problemas);
END$$ 

DELIMITER ;

CALL Realizar_Missao("Profundezas do Gigante", 2, "Após mais análises o planeta parece abrigar estruturas interessantes porém protegidas.");

SELECT * FROM Missao_Realizada;
-- =-=-=-=-=-=-=-=-=-=-=-= Procedure =-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Function =-=-=-=-=-=-=-=-=-=-=-=-=-=
DELIMITER $$ 

CREATE FUNCTION valorTotalPlaneta(planeta VARCHAR(45)) RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE total_planeta FLOAT DEFAULT 0;
    
    -- phr -> tabela planeta_has_recurso, r -> tabela recurso
    SELECT SUM(phr.quantidadeRecurso * r.valorUnitario) INTO total_planeta
    FROM Planeta_has_Recurso phr
    JOIN Recurso r ON phr.Recurso_nomeRecurso = r.nomeRecurso
    WHERE phr.Planeta_nomePlaneta = planeta;
    
    RETURN total_planeta;
END $$ 
DELIMITER ;

SELECT valorTotalPlaneta('Profundezas do Gigante');
-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Function =-=-=-=-=-=-=-=-=-=-=-=-=-=


    
-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Updates =-=-=-=-=-=-=-=-=-=-=-=-=-=
UPDATE Missao SET status = "Concluída" WHERE idMissao = 2;

UPDATE Planeta_has_Recurso SET quantidadeRecurso = 100.0 WHERE Planeta_nomePlaneta = "Abrolho Sombrio";

SELECT * FROM Missao;
SELECT * FROM Planeta_has_recurso;
-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Updates =-=-=-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Deletes =-=-=-=-=-=-=-=-=-=-=-=-=-=
DELETE FROM Planeta WHERE habitavel = 1;

DELETE FROM Planeta 
WHERE nomePlaneta IN (
    SELECT Planeta_nomePlaneta 
    FROM Planeta_has_Recurso 
    WHERE quantidadeRecurso < 200
);

SELECT * FROM Planeta;
-- =-=-=-=-=-=-=-=-=-=-=-=-=-= Deletes =-=-=-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-=-=-=  Alter  =-=-=-=-=-=-=-=-=-=-=-=-=-=
ALTER TABLE Planeta_has_Recurso MODIFY quantidadeRecurso INT NOT NULL;

SELECT * FROM Planeta_has_Recurso;
-- =-=-=-=-=-=-=-=-=-=-=-=-=-=  Alter  =-=-=-=-=-=-=-=-=-=-=-=-=-=



-- =-=-=-=-=-=-=-=-=-=-=-=-=-=   Drop   =-=-=-=-=-=-=-=-=-=-=-=-=-=
DROP TABLE Missao_Realizada;
-- =-=-=-=-=-=-=-=-=-=-=-=-=-=   Drop   =-=-=-=-=-=-=-=-=-=-=-=-=-=

