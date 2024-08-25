import sqlite3

#Conectar ao db
def connect():
    con = sqlite3.connect('dados.db')
    return con

#Função para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    con = connect()
    con.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                 VALUES (?, ?, ?, ?, ?)",(titulo, autor, editora, ano_publicacao, isbn) )
    con.commit()
    con.close()
    
#Função para inserir usuarios
def insert_user(nome, sobrenome, endereco, email, telefone):
    con = connect ()
    con.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                 VALUES(?, ?, ?, ?, ?)",(nome, sobrenome, endereco, email, telefone))
    con.commit()
    con.close()

# Função para exibir usuarios
def get_user():
    con = connect()
    c = con.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    con.close()
    return users

 #Função para exibir os livros
def exibir_livros():
    con = connect()
    livros = con.execute("SELECT * FROM livros").fetchall()
    con.close()

    return livros


exibir_livros()

# função para realizara imprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    con = connect()
    con.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                VALUES(?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    
    con.commit()
    con.close()

# Funçao para exibir todos os livros emprestado no momento
def get_books_on_loan():
    con = connect()
    result = con.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                           FROM livros\
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                           WHERE emprestimos.data_devolucao IS NULL").fetchall()
    con.close()
    return result

print(get_books_on_loan())

# Funcao para atualizar a data de devolucao de emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    con = connect()
    con.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (id_emprestimo, data_devolucao))
    con.commit()
    con.close()

# Exemplo de das funçoes
#insert_book("Dom Quixote", "Miquel", "Editora 1", 1605, "123456")
#insert_user("Joao", "Mello", "Argentina,BuenoAires", "joaomello@gmail.com", "+244 123")  
#insert_loan(1,1,"2024-08-21", None)
livros_emprestados = get_books_on_loan()

print(livros_emprestados)

#update_loan_return_date(1,"2024-08-21")
#exibir_livros()
