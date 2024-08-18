import customtkinter as tk
from tkinter import ttk
import crud as crud


class principalBD:
    def __init__(self, win):
        self.obgBD = crud.AppBD()

        #conponentes



        self.frame_1 = tk.CTkFrame(win, width=800, height=200, fg_color='#dfe3ee')
        self.frame_2 = tk.CTkFrame(win, width=800,height=400,fg_color='#dfe3ee',border_width=3,border_color='black')


        self.lblnome=tk.CTkLabel(self.frame_1, text="nome do aluno:", text_color='black')
        self.lblidade=tk.CTkLabel(self.frame_1, text="idade do aluno:", text_color='black')


        self.txtnome=tk.CTkEntry(self.frame_1)
        self.txtidade=tk.CTkEntry(self.frame_1)
        self.btncadastrar=tk.CTkButton(self.frame_1, text="Cadastrar", command=self.fcadastraraluno )
        self.btnatualizar=tk.CTkButton(self.frame_1, text="Atualizar",command=self.fatualizaralunos)
        self.btnexcluir=tk.CTkButton(self.frame_1, text="Excluir",command=self.fexcluiralunos)
        self.btnlimpar=tk.CTkButton(self.frame_1, text="Limpar", command=self.flimpartela)



        #----------- componentes Treeview ---------

        self.dadoscolunas = ("id","nome","idade")

        self.treealunos = ttk.Treeview(self.frame_2, columns=self.dadoscolunas,selectmode='browse')

        self.verscrbar = ttk.Scrollbar(self.frame_2,orient="vertical",command=self.treealunos.yview)
        self.verscrbar.pack(side ='right',fill='x')

        self.treealunos.configure(yscrollcommand=self.verscrbar.set)

        self.treealunos.heading("#0", text="")
        self.treealunos.heading("id", text="ID")
        self.treealunos.heading("nome", text="NOME")
        self.treealunos.heading("idade", text="IDADE")

        self.treealunos.column("#0",width=1)
        self.treealunos.column("id",width=50, anchor='center')
        self.treealunos.column("nome", width=100)
        self.treealunos.column("idade", width=100, anchor='center')



        self.treealunos.bind("<<treeviewselect>>",self.apresentarregistrosselecionados)



        #--------posicionamento dos componetes na janela ---------

        self.frame_1.place(relx=0.01, rely=0)
        self.frame_2.place(relx=0.01, rely=0.33)


        self.lblnome.place(relx=0.03,rely=0.03)
        self.lblidade.place(relx=0.03,rely=0.20)

        self.txtnome.place(relx=0.20,rely=0.03)
        self.txtidade.place(relx=0.20,rely=0.20)

        self.btncadastrar.place(relx=0,rely=0.45)
        self.btnatualizar.place(relx=0.20,rely=0.45)
        self.btnexcluir.place(relx=0,rely=0.65)
        self.btnlimpar.place(relx=0.20,rely=0.65)




        self.treealunos.place(relx=0.01,rely=0.05, relwidth=0.96,relheight=0.90)
        self.verscrbar.place(relx=0.95,rely=0.05, height=450)
        self.carregardadosiniciais()



    #--------------------#####---------
    def apresentarregistrosselecionados(self,event):
        self.flercampos()
        for selection in self.treealunos.selection():
            item = self.treealunos.item(selection)
            nome,idade= item["values"] [0:3]
            self.txtnome.insert(0,nome)
            self.txtidade.insert(0,idade)

    def carregardadosiniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.obgBD.selecionardados()
            print("**********dados disponiveis *********")
            for item in registros:
                id=item[0]
                nome=item[1]
                idade=item[2]
                print("nome =",nome)
                print("idade =",idade)

                self.treealunos.insert('','end',iid=self.iid,values=(id,nome,idade))
                self.iid = self.iid +1
                self.id = self.id + 1
                print("dados da base")
        except:
            print('ainda não existem dados para carregar')


    def flercampos(self):
        try:
            print("********* dados disponiveis *********")
            nome = self.txtnome.get()
            print("nome",nome)
            idade=int(self.txtidade.get())
            print("idade",idade)
            print("leitura dos dados com sucesso.")
        except:
            print("não foi possivel ler os dados.")
        return nome, idade


    def fcadastraraluno(self):
        try:
            print('******* dados disponiveis*********')
            nome, idade = self.flercampos()
            self.obgBD.inserirdados(nome,idade)
            self.treealunos.insert('','end',iid=self.iid,values=(nome,idade))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.flimpartela()
            print('produto cadastrado com sucesso!')
        except:
            print("não foi possivel fazer o cadastro")

    def flimpartela(self):
        try:
            print("******dados disponiveis *******")
            self.txtnome.delete(0,tk.END)
            self.txtidade.delete(0,tk.END)
            print("campo limpo!")
        except:
            print("não foi possivel limpar os campos.")

    def fatualizaralunos(self):
        try:
            print("********** dados disponiveis **********")
            nome, idade = self.flercampos()
            self.obgBD.atualizardados(nome,idade)

            self.treealunos.delete(*self.treealunos.get_children())
            self.carregardadosiniciais()
            self.flimpartela()
            print('aluno atualixzado com sucesso!')
        except:
            print('não foi possivel fazer a atualização')


    def fexcluiralunos(self):
        try:
            print("********** dados disponoveis ***********")
            nome, idade = self.flercampos()
            self.obgBD.excluirdados(nome)

            self.treealunos.delete(*self.treealunos.get_children())
            self.carregardadosiniciais()
            self.flimpartela()
            print('aluno excluido com sucesso!')
        except:
            print("não foi possivel fazer a exclusão do aluno")






janela = tk.CTk()
principal=principalBD(janela)
janela.title('agenda de alunos')
janela.geometry("820x600")
janela.mainloop()