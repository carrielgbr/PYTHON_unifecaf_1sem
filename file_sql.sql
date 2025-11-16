-- drop database little_marketplace;
-- Comando inicial para criar e usar o banco de dados do projeto
CREATE DATABASE IF NOT EXISTS eletric_shop;
USE eletric_shop;

CREATE TABLE tbl_admin(
	id_admin INT PRIMARY KEY AUTO_INCREMENT,
    nome_admin VARCHAR (100),
    pass_admin VARCHAR (10),
    DATA_CAD DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tbl_admin (nome_admin,pass_admin) VALUES ('admin01','admin01');
SET @ID_USER_ADMIN = LAST_INSERT_ID();

SELECT * FROM tbl_admin;

CREATE TABLE tbl_users(
	id_users INT PRIMARY KEY AUTO_INCREMENT,
    nome_user VARCHAR (100),
    pass_user VARCHAR (100),
    
    id_admin INT
);

INSERT INTO tbl_users (nome_user, pass_user, id_admin) VALUES ('allan', 'allan', @ID_USER_ADMIN);
SET @ID_USER_ALLAN = LAST_INSERT_ID();

INSERT INTO tbl_users (nome_user, pass_user, id_admin) VALUES ('carriel', 'carriel', @ID_USER_ADMIN);
SET @ID_USER_CARRIEL = LAST_INSERT_ID();

SELECT * FROM tbl_users;
 
 -- 1. Cria a nova tabela de Histórico
CREATE TABLE tbl_historico(
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP, -- Quando a ação ocorreu
    
    -- ID do usuário que executou a ação (pode ser um Admin ou um User)
    id_executor INT NOT NULL,                     
    
    -- Tipo de executor (A = Admin, U = User)
    tipo_executor CHAR(1) NOT NULL,              
    
    acao VARCHAR(255),                          -- O que foi feito (ex: 'CADASTRO NOVO USER')
    tabela_afetada VARCHAR(50),                 -- A tabela que recebeu a inserção (ex: 'tbl_users', 'tbl_admin')
    id_objeto_afetado INT,                      -- ID do objeto (usuário, produto) que foi criado/modificado
    tela_origem VARCHAR(100)                    -- De qual tela do programa a ação partiu (ex: 'UserManagementScreen')
);
 
DELIMITER //

CREATE TRIGGER trg_admin_insert_history
AFTER INSERT ON tbl_admin
FOR EACH ROW
BEGIN
    -- Assume que o primeiro admin (ID 1) é o responsável por ações externas (via MySQL CLI)
    INSERT INTO tbl_historico (id_executor, tipo_executor, acao, tabela_afetada, id_objeto_afetado, tela_origem)
    VALUES (
        1, -- ID do Admin padrão (ajuste se o ID do admin01 for diferente)
        'A',
        'CADASTRO NOVO ADMIN',
        'tbl_admin',
        NEW.id_admin,
        'MYSQL_CLI'
    );
END;
//

-- Restaura o delimitador padrão
DELIMITER ;

SELECT
    H.data_hora,
    H.acao,
    H.tabela_afetada,
    H.tela_origem,
    -- Usa CASE para determinar se o executor é Admin ou User
    CASE H.tipo_executor
        WHEN 'A' THEN ADM.nome_admin
        WHEN 'U' THEN USR.nome_user
        ELSE 'N/D'
    END AS nome_executor
FROM 
    tbl_historico H
-- Tenta dar JOIN com Administradores
LEFT JOIN 
    tbl_admin ADM ON H.id_executor = ADM.id_admin AND H.tipo_executor = 'A'
-- Tenta dar JOIN com Usuários Comuns
LEFT JOIN 
    tbl_users USR ON H.id_executor = USR.id_users AND H.tipo_executor = 'U'
ORDER BY
    H.data_hora DESC;
 

 SELECT * FROM tbl_admin;
 SELECT * FROM tbl_users;
 show tables; 
 
DROP DATABASE eletric_shop;