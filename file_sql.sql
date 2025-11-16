-- drop database little_marketplace;
-- Comando inicial para criar e usar o banco de dados do projeto
CREATE DATABASE IF NOT EXISTS eletric_shop;
USE eletric_shop;

CREATE TABLE tbl_admin(
	id_admin INT PRIMARY KEY AUTO_INCREMENT,
    nome_admin VARCHAR (100),
    pass_admin VARCHAR (10)
);

INSERT INTO tbl_admin (nome_admin,pass_admin) VALUES ('admin','admin');
SET @ID_USER_ADMIN = LAST_INSERT_ID();

SELECT * FROM tbl_admin;