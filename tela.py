from tkinter import messagebox
from tkinter import ttk
from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk
from view import *

cor0 = "#2e2d2b" # Preta
cor1 = "#feffff" # Branca
cor2 = "#4fa882" # Verde
cor3 = "#38576b" # Valor
cor4 = "#403d3d" # letra
cor5 = "#e06636" # -Profit
cor6 = "#0035e3" # Azul
cor7 = "#3fbfb9" # Verde
cor8 = "#263238" # + Verde
cor9 = "#e9edf5" # + verde
cor10 = "#6e8faf" #
cor11 = "f2f4f2"

# Criando Janela---------------------------------------------------------------------------------------------------------------------------------------------------
janela = Tk()
janela.title("")
janela.geometry('770x340')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

Style = Style(janela)
Style.theme_use("clam")

#Frame tela----------------------------------------------------------------------------------------------------------------------------------------------------------

frameCima = Frame(janela, width=770, height=50, bg=cor6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=cor4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita =  Frame(janela, width=600, height=265, bg=cor1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# Logo
#Abrindo img
app_img = Image.open('logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=cor6, fg=cor1)
app_logo.place(x=5, y=0)

app_logo = Label(frameCima, text= "Sistema de gerenciamento de livros" , compound=LEFT, padx=5, anchor=NW,font=('Verdana 15 bold'), bg=cor6, fg=cor1)
app_logo.place(x=50, y=7)

app_linha = Label(frameCima, width=770 ,height=1, padx=5, anchor=NW,font=('Verdana 1 bold'), bg=cor3, fg=cor1)
app_linha.place(x=0, y=47)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def novo_usuario():

    global img_salvar

    def add():
        first_name = e_p_nome.get()
        last_name = e_sobrenome.get()
        address = e_endereco.get()
        email = e_email.get()
        phone = e_telefone.get()

        lista = [first_name, last_name, address, email, phone]

        # Vereficar caso algum campo esteja vazio ou nao
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', "Preencha todos os campos")
                return
            

        #Inserindo Banco de Dados
        insert_user(first_name, last_name, address, email, phone)

        messagebox.showinfo('Sucesso', 'Usuario inserido')

        #Limpando campos de entrada
        e_p_nome.delete(0, END)
        e_sobrenome.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)


    app_ =  Label(frameDireita, text="Inserir um novo usuario", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg= cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW) 
    app_ =  Label(frameDireita, text="Inserir um novo usuario", width=400, height=1, anchor=NW ,font=('Verdana 1'), bg= cor3, fg=cor1)
    app_.grid(row=1, column=0, columnspan=4, sticky=NSEW) 

    l_p_nome =  Label(frameDireita, text="Primeiro nome:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_p_nome =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_nome.grid(row=2, column=1, padx=5, pady=10 ,sticky=NSEW) 


    l_sobrenome =  Label(frameDireita, text="Sobrenome:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_sobrenome.grid(row=3, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_sobrenome =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_sobrenome.grid(row=3, column=1, padx=5, pady=10 ,sticky=NSEW) 

    l_endereco =  Label(frameDireita, text="Endereço do usuário:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_endereco.grid(row=4, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_endereco =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_endereco.grid(row=4, column=1, padx=5, pady=10 ,sticky=NSEW) 

    l_email =  Label(frameDireita, text="Email:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_email.grid(row=5, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_email =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_email.grid(row=5, column=1, padx=5, pady=10 ,sticky=NSEW) 

    l_telefone=  Label(frameDireita, text="Numero de Telefone:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_telefone.grid(row=6, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_telefone = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_telefone.grid(row=6, column=1, padx=5, pady=10 ,sticky=NSEW) 

    img_salvar = Image.open('add.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar )
    b_salvar = Button(frameDireita, command=add ,image=img_salvar, compound=LEFT, anchor=NW, width=100, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# Ver usuario
def ver_usuarios():
    
    app_ =  Label(frameDireita, text="Exibir usuários", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg= cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW) 
    app_ =  Label(frameDireita, text="Exibir usuários", width=400, height=1, anchor=NW ,font=('Verdana 1'), bg= cor3, fg=cor1)
    app_.grid(row=1, column=0, columnspan=4, sticky=NSEW) 

    dados = get_user()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# Novo Livro
def novo_livro():

    global img_salvar

    def add():
        
        title = e_titulo.get()
        author = e_autor.get()
        publisher = e_editora.get()
        year = e_ano.get()
        isbn = e_isbn.get()

        lista = [title, author, publisher, year, isbn]


        # Vereficar caso algum campo esteja vazio ou nao
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', "Preencha todos os campos")
                return
            

        #Inserindo Banco de Dados
        insert_book(title, author, publisher, year, isbn)

        messagebox.showinfo('Sucesso', 'Livro inserido')

        #Limpando campos de entrada
        e_titulo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_isbn.delete(0, END)


    app_ =  Label(frameDireita, text="Inserir um novo livro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg= cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW) 
    app_ =  Label(frameDireita, text="Inserir um novo livro", width=400, height=1, anchor=NW ,font=('Verdana 1'), bg= cor3, fg=cor1)
    app_.grid(row=1, column=0, columnspan=4, sticky=NSEW) 

    l_titulo =  Label(frameDireita, text="Titulo do Livro:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_titulo.grid(row=2, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_titulo =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_titulo.grid(row=2, column=1, padx=5, pady=10 ,sticky=NSEW) 


    l_autor =  Label(frameDireita, text="Autor do Livro:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_autor.grid(row=3, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_autor =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=10 ,sticky=NSEW) 

    l_editora =  Label(frameDireita, text="Editora do Livro:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_editora.grid(row=4, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_editora =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=10 ,sticky=NSEW) 

    l_ano =  Label(frameDireita, text="Ano de Publicação do Livro:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_ano.grid(row=5, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_ano =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_ano.grid(row=5, column=1, padx=5, pady=10 ,sticky=NSEW) 

    l_isbn=  Label(frameDireita, text="ISBN do Livro:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_isbn.grid(row=6, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_isbn = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_isbn.grid(row=6, column=1, padx=5, pady=10 ,sticky=NSEW) 

    img_salvar = Image.open('add.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar )
    b_salvar = Button(frameDireita, command=add ,image=img_salvar, compound=LEFT, anchor=NW, width=100, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# Função ver livros

def ver_livros():

    app_ =  Label(frameDireita, text="Todos Livros", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg= cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW) 
    app_ =  Label(frameDireita, width=400, height=1, anchor=NW ,font=('Verdana 1'), bg= cor3, fg=cor1)
    app_.grid(row=1, column=0, columnspan=4, sticky=NSEW) 

    dados = exibir_livros()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Titulo','Autor','Editora','Ano','ISBN']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,165,110,100,50,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def realizar_emprestimo():

    global img_salvar

    def add():

        user_id = e_id_usuario.get()
        book_id = e_id_livro.get()

        lista = [user_id, book_id]


        #Verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha  todos os campos')
                return
            
        # Inserindo os dados no banco de dados
        insert_loan(user_id, book_id, NONE)

        messagebox.showinfo('Sucesso', 'Livro inserido com sucesso')

        #Limpando os campos de entradas
        e_id_usuario.delete(0, END)
        e_id_livro.delete(0, END)
    
    app_ =  Label(frameDireita, text="Realizar um emprestimo", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg= cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW) 
    app_linha=  Label(frameDireita, width=400, height=1, anchor=NW ,font=('Verdana 1'), bg= cor3, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW) 

    l_id_usuario =  Label(frameDireita, text="Digite o ID do usuario:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_id_usuario.grid(row=2, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_id_usuario =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_usuario.grid(row=2, column=1, padx=5, pady=10 ,sticky=NSEW) 


    l_id_livro =  Label(frameDireita, text="Difite o ID do livro:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_id_livro.grid(row=3, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_id_livro =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_livro.grid(row=3, column=1, padx=5, pady=10 ,sticky=NSEW) 


    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar )
    b_salvar = Button(frameDireita, command=add ,image=img_salvar, compound=LEFT, anchor=NW, width=100, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def ver_livros_emprestados():

    app_ =  Label(frameDireita, text="Livros Emprestados", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg= cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW) 
    app_ =  Label(frameDireita, width=400, height=1, anchor=NW ,font=('Verdana 1'), bg= cor3, fg=cor1)
    app_.grid(row=1, column=0, columnspan=4, sticky=NSEW) 

    dados = ver_livros_emprestados()

        #creating a treeview with dual scrollbars
    list_header = ['ID','Titulo','Nome do Usuario','D.emprestimo','D.devolução']

    get_books_on_loan = get_books_on_loan()

    for book in get_books_on_loan:
        dado =[f"{book[0]}", f"{book[1]}", f"{book[2]}", f"{book[3]}", f"{book[4]}", f"{book[5]}"]

        dados.append(dado)
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","ne","ne","ne","ne"]
    h=[20,165,110,100,50,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

# Devolução de um Emprestimo
def devolucao_emprestimo():

    global img_salvar

    def add():

        loan_id = e_id_emprestimo.get()
        return_date = e_data_retorno.get()

        lista = [loan_id, return_date]


        #Verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha  todos os campos')
                return
            
        # Inserindo os dados no banco de dados
        update_loan_return_date(loan_id, return_date)

        messagebox.showinfo('Sucesso', 'Livro retornado com sucesso')

        #Limpando os campos de entradas
        e_id_emprestimo.delete(0, END)
        e_data_retorno.delete(0, END)
    
    app_ =  Label(frameDireita, text="Atualizar a data de devolução de um emprestimo", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg= cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW) 
    app_linha=  Label(frameDireita, width=400, height=1, anchor=NW ,font=('Verdana 1'), bg= cor3, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW) 

    l_id_emprestimo =  Label(frameDireita, text="ID do emprestimo:", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_id_emprestimo =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=10 ,sticky=NSEW) 


    l_data_retorno =  Label(frameDireita, text="Nova data de devolução (formato: AAAA-MM-DD):", anchor= NW,font=('Ivy 10'), bg= cor1, fg=cor4)
    l_data_retorno.grid(row=3, column=0, padx=5, pady=10 ,sticky=NSEW) 
    e_data_retorno =  Entry(frameDireita, width=25, justify='left', relief='solid')
    e_data_retorno.grid(row=3, column=1, padx=5, pady=10 ,sticky=NSEW) 


    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar )
    b_salvar = Button(frameDireita, command=add ,image=img_salvar, compound=LEFT, anchor=NW, width=100, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW)
        
    



# Função para controlar menu
def control(i):

    # Novo Usuario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Função    
        novo_usuario()

    #Ver usuario
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Função    
        ver_usuarios()

     # Novo livro
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Função    
        novo_livro()
    
    # Ver Livros
    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Função    
        ver_livros()
    
    # Realizar emprestimo
    if i =='realizar_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        #Chamando Função
        realizar_emprestimo()

    #Ver livros emprestado
    if i =='ver_livros_emprestados':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        #Chamando Função
        ver_livros_emprestados()
        

    # Retorno do emprestimo
    if i =='Retorno':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        #Chamando Função
        devolucao_emprestimo()   

    




# Menu

#Novo usuario
img_usuario = Image.open('add.png')
img_usuario = img_usuario.resize((18,18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command=lambda:control('novo_usuario') ,image=img_usuario, compound=LEFT, anchor=NW, text=' Novo usuario', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

#Novo Livro
img_novo_livro= Image.open('add.png')
img_novo_livro= img_novo_livro.resize((18,18))
img_novo_livro= ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, command=lambda:control('novo_livro'), image=img_usuario, compound=LEFT, anchor=NW, text=' Novo livro', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Livro
img_ver_livro= Image.open('logo.png')
img_ver_livro= img_ver_livro.resize((18,18))
img_ver_livro= ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerda, command=lambda:control('ver_livros') ,image=img_ver_livro, compound=LEFT, anchor=NW, text=' Exibir todos livros', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Usuarios
img_ver_usuario= Image.open('user.png')
img_ver_usuario= img_ver_usuario.resize((18,18))
img_ver_usuario= ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text=' Exibir todos usuarios', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

#Realizar Emprestimo
img_emprestimo= Image.open('add.png')
img_emprestimo= img_emprestimo.resize((18,18))
img_emprestimo= ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, command=lambda:control('realizar_emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text=' Realizar emprestimo', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução de um Emprestimo
img_devolucao= Image.open('update.png')
img_devolucao= img_devolucao.resize((18,18))
img_devolucao= ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, command=lambda:control('Retorno'), image=img_devolucao, compound=LEFT, anchor=NW, text=' Devolução de um emprestimo', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Livro emprestado no momento
img_livros_emprestado= Image.open('sell.png')
img_livros_emprestado= img_livros_emprestado.resize((18,18))
img_livros_emprestado= ImageTk.PhotoImage(img_livros_emprestado)
b_livros_emprestado = Button(frameEsquerda,command=lambda:control('ver_livros_emprestados'), image=img_livros_emprestado, compound=LEFT, anchor=NW, text=' Livro emprestados', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestado.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

janela.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------