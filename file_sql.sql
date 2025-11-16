-- drop database little_marketplace;
-- Comando inicial para criar e usar o banco de dados do projeto
CREATE DATABASE IF NOT EXISTS eletric_shop;
USE eletric_shop;

CREATE TABLE tbl_admin(
	id_admin INT PRIMARY KEY AUTO_INCREMENT,
    nome_admin VARCHAR (100),
    pass_admin VARCHAR (10)
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
 
DROP DATABASE eletric_shop;