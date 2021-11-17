from tkinter import *
from tkinter.font import Font
from tkinter import ttk

from funcs import Funcs
from relatorios import Relats


root = Tk()

font = Font(family='Verdana', size=9, weight='bold')
font_bold = Font(family='Alef', size=10, weight='bold')
font_input = Font(family='Arial', size=10, weight='bold')


class Application(Funcs, Relats):
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
        # self.root.iconbitmap('./favicon.ico')
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
        # Abas;;;
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background='#eeeeee')
        self.aba2.configure(background='#eeeee5')

        self.abas.add(self.aba1, text='Aba 1')
        self.abas.add(self.aba2, text='Aba 2')

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)



        # botão exemplo Canvas;
        self.bt_canvas = Canvas(self.aba1, bd=0, bg='#2e6783', highlightbackground='grey',
                                highlightthickness=1)
        self.bt_canvas.place(relx=0.19, rely=0.08, relwidth=0.23, relheight=0.19)
        # botão Limpar;
        self.bt_limpar = Button(self.aba1, text='Limpar', activebackground='#108ecb',
                                font=font, bd=3, bg='#125080', fg='#fff',
                                command=self.limpar)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)


        balao_msg = 'Limpa os Campos de Cadastro'
        # self.limpar_balloon = tix.Balloon(self.aba1, initwait=600)
        # self.limpar_balloon.bind_widget(self.bt_limpar, balloonmsg=balao_msg)


        # botão Buscar;
        self.bt_buscar = Button(self.aba1, text='Buscar',
                                font=font, bd=3, bg='#125080', fg='#fff',
                                command=self.buscaCliente)
        self.bt_buscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)

        msg_balloon = 'Digite no campo Nome o Cliente a Pesquisar.'
        # self.buscar_balao = tix.Balloon(self.aba1, initwait=600)
        # self.buscar_balao.bind_widget(self.bt_buscar, balloonmsg=msg_balloon)


        # botão Novo;
        self.bt_novo = Button(self.aba1, text='Novo', font=font,
                              bd=3, bg='#125080', fg='#fff',
                              command=self.addCliente)
        self.bt_novo.place(relx=0.61, rely=0.1, relwidth=0.1, relheight=0.15)


        msg_novo = 'Adiciona um novo Cliente'
        # self.novo_balloon = tix.Balloon(self.aba1, initwait=600)
        # self.novo_balloon.bind_widget(self.bt_novo, balloonmsg=msg_novo)


        # botão Alterar;
        self.bt_alterar = Button(self.aba1, text='Alterar',
                                 font=font, bd=3, bg='#125080', fg='#fff',
                                 command=self.alterarCliente)
        self.bt_alterar.place(relx=0.72, rely=0.1, relwidth=0.1, relheight=0.15)

        msg_alterar = 'Altera os dados de um Cliente'
        # self.alterar_balloon = tix.Balloon(self.aba1, initwait=600)
        # self.alterar_balloon.bind_widget(self.bt_alterar, balloonmsg=msg_alterar)

        # botão Apagar;
        self.bt_apagar = Button(self.aba1, text='Apagar', activebackground='#8e1e2e',
                                font=font, bd=3, bg='#125080', fg='#fff',
                                command=self.delCliente)
        self.bt_apagar.place(relx=0.83, rely=0.1, relwidth=0.1, relheight=0.15)

        msg_apagar = 'Apaga o Cliente'
        # self.apagar_balloon = tix.Balloon(self.aba1, initwait=600)
        # self.apagar_balloon.bind_widget(self.bt_apagar, balloonmsg=msg_apagar)


        # labels Códigos;
        self.labelCodigo = Label(self.aba1, text='Código',
                                 bg='#eeeeee', fg='#1e2050', font=font_bold, )
        self.labelCodigo.place(relx=0.058, rely=0.05)

        self.entryCodigo = Entry(self.aba1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryCodigo.place(relx=0.05, rely=0.165, relwidth=0.1, relheight=0.1)

        # labels Nome;
        self.labelNome = Label(self.aba1, text='Nome',
                               bg='#eeeeee', fg='#1e2050', font=font_bold, )
        self.labelNome.place(relx=0.05, rely=0.34)

        self.entryNome = Entry(self.aba1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryNome.place(relx=0.04, rely=0.45, relwidth=0.75, relheight=0.115)

        # labels Telefone;
        self.labelTelefone = Label(self.aba1, text='Telefone',
                                   bg='#eeeeee', fg='#1e2050', font=font_bold)
        self.labelTelefone.place(relx=0.05, rely=0.64)

        self.entryTelefone = Entry(self.aba1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryTelefone.place(relx=0.04, rely=0.75, relwidth=0.38, relheight=0.115)

        # labels Cidade;
        self.labelCidade = Label(self.aba1, text='Cidade',
                                 bg='#eeeeee', fg='#1e2050', font=font_bold)
        self.labelCidade.place(relx=0.58, rely=0.64)

        self.entryCidade = Entry(self.aba1, font=font_input, bg='#e0ffff', fg='#000')
        self.entryCidade.place(relx=0.58, rely=0.75, relwidth=0.38, relheight=0.115)

        # Drop Down;;;
        self.TipVar = StringVar(self.aba2)
        self.TipV = ('Solteiro(a)', 'Casado(a)')
        self.TipVar.set('Solteiro(a)')
        self.popup = OptionMenu(self.aba2, self.TipVar, *self.TipV)
        self.popup.configure(font=('Alef', 10), background='#888888', activebackground='#222222', activeforeground='#fff')
        self.popup.place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.2)
        self.estado_civil = self.TipVar.get()

        print(self.estado_civil)


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
