import sqlite3

# Conection db

con = sqlite3.connect('dados.db')

# Criar table de boocks

con.execute(' CREATE TABLE livros(\
                id INTEGER PRIMARY KEY,\
                titulo Text,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)')

# Criando Table User
con.execute(' CREATE TABLE usuarios(\
                id INTEGER PRIMARY KEY,\
                nome Text,\
                sobrenome TEXT,\
                endereco TEXT,\
                email INTEGER,\
                telefone TEXT)')

# Criando tabela de empretimos
con.execute(' CREATE TABLE emprestimos(\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')