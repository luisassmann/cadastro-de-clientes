"""
Cadastro de clientes usando Tkinter;;;
"""
# ----- Window -----
from tkinter import *
from tkinter.font import Font
from tkinter import ttk

# ----- DataBase ----
import sqlite3

# ----- PDF - generator ------
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

# -- Open Browser --
import webbrowser


root = Tk()

font = Font(family='Verdana', size=9, weight='bold')
font_bold = Font(family='Alef', size=10, weight='bold')
font_input = Font(family='Arial',size=10, weight='bold')

# -------------- PDF - generator ----------------
class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")

    def geradorRelatCliente(self):
        self.archivepdf = canvas.Canvas("./cliente.pdf")

        self.codigoRel = self.entryCodigo.get()
        self.nomeRel = self.entryNome.get()
        self.telefoneRel = self.entryTelefone.get()
        self.cidadeRel = self.entryCidade.get()

        # --- Título ---
        self.archivepdf.setFont("Helvetica-Bold", 24)
        self.archivepdf.drawString(200, 790, 'Ficha do Cliente')

        # --- Dados do Cliente ---
        self.archivepdf.setFont("Helvetica-Bold", 18)
        self.archivepdf.drawString(50, 700, 'Código: ')
        self.archivepdf.drawString(50, 670, 'Nome: ')
        self.archivepdf.drawString(50, 640, 'Telefone: ')
        self.archivepdf.drawString(50, 610, 'Cidade: ')

        self.archivepdf.setFont("Helvetica", 18)
        self.archivepdf.drawString(120, 700, self.codigoRel)
        self.archivepdf.drawString(110, 670, self.nomeRel)
        self.archivepdf.drawString(134, 640, self.telefoneRel)
        self.archivepdf.drawString(120, 610, self.cidadeRel)

        self.archivepdf.rect(20, 550, 550, 280, fill=False, stroke=True)

        self.archivepdf.showPage()
        self.archivepdf.save()
        self.printCliente()

# ---------------- BACK - END -------------------
class funcs():
    def limpar(self):
        self.entryCodigo.delete(0, END)
        self.entryNome.delete(0, END)
        self.entryTelefone.delete(0, END)
        self.entryCidade.delete(0, END)

    def conectarDB(self):
        self.conn = sqlite3.connect('./clientes.db')
        self.cursor = self.conn.cursor()
        print('Conectando ao Banco de Dados...')

    def desconectarDB(self):
        self.conn.close()
        print('Desconectando o Banco de Dados...')

    def montaTabelas(self):
        self.conectarDB()

        # -- Criação da Tabela --

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)

        self.conn.commit(), print("Banco de Dados Criado...")
        self.desconectarDB()

    def variaveis(self):
        self.codigo = self.entryCodigo.get()
        self.nome = self.entryNome.get()
        self.telefone = self.entryTelefone.get()
        self.cidade = self.entryCidade.get()

    def addCliente(self):
        self.variaveis()
        self.conectarDB()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))

        self.conn.commit()
        self.desconectarDB()
        self.selectLista()
        self.limpar()

    def selectLista(self):
        self.listaUser.delete(*self.listaUser.get_children())
        self.conectarDB()

        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaUser.insert("", END, values=i)

        self.desconectarDB()

    def duploClick(self, event):
        self.limpar()
        self.listaUser.selection()

        for n in self.listaUser.selection():
            col1, col2, col3, col4 = self.listaUser.item(n, 'values')
            self.entryCodigo.insert(END, col1)
            self.entryNome.insert(END, col2)
            self.entryTelefone.insert(END, col3)
            self.entryCidade.insert(END, col4)

    def delCliente(self):
        self.variaveis()
        self.conectarDB()

        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo,))
        self.conn.commit()

        self.desconectarDB()
        self.limpar()
        self.selectLista()

    def alterarCliente(self):
        self.variaveis()
        self.conectarDB()

        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? WHERE cod = ? """,
                            (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()

        self.desconectarDB()
        self.selectLista()
        self.limpar()

    def buscaCliente(self):
        self.conectarDB()
        self.listaUser.delete(*self.listaUser.get_children())

        self.entryNome.insert(END, '%')
        nome = self.entryNome.get()

        self.cursor.execute("""
            SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)

        buscaNomeCliente = self.cursor.fetchall()
        for i in buscaNomeCliente:
            self.listaUser.insert("", END, values=i)

        self.limpar()
        self.desconectarDB()

# ---------------- FRONT - END ------------------
class Application(funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgetsFrame1()
        self.listaFrame2()
        self.montaTabelas()
        self.selectLista()
        self.Menus()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro')
        self.root.configure(background='#1e2050')
        self.root.geometry('700x500')
        self.root.iconbitmap('./favicon.ico')
        self.root.resizable(True, True)
        self.root.minsize(width=700, height=400)

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg='#eeeeee',
                            highlightbackground='#4600FF',
                            highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)

        self.frame2 = Frame(self.root, bd=4, bg='#eeeeee',
                            highlightbackground='#4600FF',
                            highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)

    def widgetsFrame1(self):
        # botão exemplo Canvas;
        self.bt_canvas = Canvas(self.frame1, bd=0, bg='#2e6783', highlightbackground='grey',
                                highlightthickness=1)
        self.bt_canvas.place(relx=0.19, rely=0.08, relwidth=0.23, relheight=0.19)
        # botão Limpar;
        self.bt_limpar = Button(self.frame1, text='Limpar', activebackground='#108ecb',
                                font=font, bd=3, bg='#125080', fg='#fff',
                                command=self.limpar)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Buscar;
        self.bt_buscar = Button(self.frame1, text='Buscar',
                                font=font, bd=3, bg='#125080', fg='#fff',
                                command=self.buscaCliente)
        self.bt_buscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Novo;
        self.bt_novo = Button(self.frame1, text='Novo',font=font,
                              bd=3, bg='#125080', fg='#fff',
                              command=self.addCliente)
        self.bt_novo.place(relx=0.61, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Alterar;
        self.bt_alterar = Button(self.frame1, text='Alterar',
                                font=font, bd=3, bg='#125080', fg='#fff',
                                 command=self.alterarCliente)
        self.bt_alterar.place(relx=0.72, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Apagar;
        self.bt_apagar = Button(self.frame1, text='Apagar',activebackground='#8e1e2e',
                                font=font, bd=3, bg='#125080', fg='#fff',
                                command=self.delCliente)
        self.bt_apagar.place(relx=0.83, rely=0.1, relwidth=0.1, relheight=0.15)


        # labels Códigos;
        self.labelCodigo = Label(self.frame1, text='Código',
                                 bg='#eeeeee',fg='#1e2050', font=font_bold,)
        self.labelCodigo.place(relx=0.058, rely=0.05)

        self.entryCodigo = Entry(self.frame1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryCodigo.place(relx=0.05, rely=0.165, relwidth=0.1, relheight=0.1)

        # labels Nome;
        self.labelNome = Label(self.frame1, text='Nome',
                                 bg='#eeeeee',fg='#1e2050', font=font_bold, )
        self.labelNome.place(relx=0.05, rely=0.34)

        self.entryNome = Entry(self.frame1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryNome.place(relx=0.04, rely=0.45, relwidth=0.75, relheight=0.115)

        # labels Telefone;
        self.labelTelefone = Label(self.frame1, text='Telefone',
                                   bg='#eeeeee',fg='#1e2050', font=font_bold)
        self.labelTelefone.place(relx=0.05, rely=0.64)

        self.entryTelefone = Entry(self.frame1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryTelefone.place(relx=0.04, rely=0.75, relwidth=0.38, relheight=0.115)

        # labels Cidade;
        self.labelCidade = Label(self.frame1, text='Cidade',
                                 bg='#eeeeee',fg='#1e2050', font=font_bold)
        self.labelCidade.place(relx=0.58, rely=0.64)

        self.entryCidade = Entry(self.frame1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryCidade.place(relx=0.58, rely=0.75, relwidth=0.38, relheight=0.115)

    def listaFrame2(self):
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", bd=1, font=('Alef', 11))  # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Alef', 11, 'bold'))  # Modify the font of the headings

        self.listaUser = ttk.Treeview(self.frame2, height=3,
                                      column=('col1', 'col2', 'col3', 'col4'),
                                      style='mystyle.Treeview')
        self.listaUser.heading('#0', text='')
        self.listaUser.heading('#1', text='Codigo')
        self.listaUser.heading('#2', text='Nome')
        self.listaUser.heading('#3', text='Telefone')
        self.listaUser.heading('#4', text='Cidade')

        self.listaUser.column('#0', width=1)
        self.listaUser.column('#1', width=35)
        self.listaUser.column('#2', width=200)
        self.listaUser.column('#3', width=100)
        self.listaUser.column('#4', width=50)

        self.listaUser.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.88)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaUser.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.05, relwidth=0.035, relheight=0.88)

        self.listaUser.bind("<Double-1>", self.duploClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu1 = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit():
            self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu1)
        menubar.add_cascade(label="Relatórios", menu=filemenu2)

        filemenu1.add_command(label="Sair", command=Quit)
        filemenu1.add_command(label="Limpar Tela", command=self.limpar)

        filemenu2.add_command(label='Ficha do cliente', command=self.geradorRelatCliente)


Application()
