CREATE TABLE usuarios (
    nome varchar(20) NOT NULL,
    nickname varchar(8) NOT NULL,
    senha varchar(100) NOT NULL,
    PRIMARY KEY (nickname)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
INSERT INTO usuarios (nome, nickname, senha) VALUES ('admin', 'admin', 'admin');
INSERT INTO usuarios (nome, nickname, senha) VALUES ('user', 'user', 'user');
INSERT INTO usuarios (nome, nickname, senha) VALUES ('user', 'user', 'user');