from tkinter import *


class Cadastro:
    def __init__(self, master=None) -> None:
        self.fontePadrao=("Arial","10")

        self.containerNome = Frame(master)
        self.containerNome["padx"] = 20
        self.containerNome.pack()
        self.nomeLabel = Label(self.containerNome, text="Nome", font= self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome= Entry(self.containerNome)
        self.nome["font"]=self.fontePadrao
        self.nome.pack(side=LEFT)

        self.containerRua = Frame(master)
        self.containerRua["padx"] = 20
        self.containerRua.pack()
        self.senhaLabel = Label(self.containerRua,text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha= Entry(self.containerRua)
        self.senha["font"]=self.fontePadrao
        self.senha.pack(side=LEFT)

        self.containerRua = Frame(master)
        self.containerRua["padx"] = 20
        self.containerRua.pack()
        self.ruaLabel = Label(self.containerRua,text="Rua   ", font=self.fontePadrao)
        self.ruaLabel.pack(side=LEFT)
        self.rua= Entry(self.containerRua)
        self.rua["font"]=self.fontePadrao
        self.rua.pack(side=LEFT)

        self.containerNumero = Frame(master)
        self.containerNumero["padx"] = 20
        self.containerNumero.pack()
        self.numeroLabel = Label(self.containerNumero,text="Número", font=self.fontePadrao)
        self.numeroLabel.pack(side=LEFT)
        self.numero= Entry(self.containerNumero)
        self.numero["font"]=self.fontePadrao
        self.numero.pack(side=LEFT)

        self.containerBairro = Frame(master)
        self.containerBairro["padx"] = 20
        self.containerBairro.pack()
        self.bairroLabel = Label(self.containerBairro,text="Bairro", font=self.fontePadrao)
        self.bairroLabel.pack(side=LEFT)
        self.bairro= Entry(self.containerBairro)
        self.bairro["font"]=self.fontePadrao
        self.bairro.pack(side=LEFT)

        self.containerCep = Frame(master)
        self.containerCep["padx"] = 20
        self.containerCep.pack()
        self.cepLabel = Label(self.containerCep,text="CEP   ", font=self.fontePadrao)
        self.cepLabel.pack(side=LEFT)
        self.cep= Entry(self.containerCep)
        self.cep["font"]=self.fontePadrao
        self.cep.pack(side=LEFT)

        self.containerTelefone = Frame(master)
        self.containerTelefone["padx"] = 20
        self.containerTelefone.pack()
        self.telefoneLabel = Label(self.containerTelefone,text="Telefone", font=self.fontePadrao)
        self.telefoneLabel.pack(side=LEFT)
        self.senha= Entry(self.containerTelefone)
        self.senha["font"]=self.fontePadrao
        self.senha.pack(side=LEFT)

        self.containerCpf =Frame(master)
        self.containerCpf["padx"] = 20
        self.containerCpf.pack()
        self.cpfLabel = Label(self.containerCpf,text="CPF   ", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)
        self.cpf= Entry(self.containerCpf)
        self.cpf["font"]=self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.containerBotao = Frame(master)
        self.containerBotao.pack()
        self.containerBotao["pady"]=10
        self.botaoCadastrar = Button(self.containerBotao)
        self.botaoCadastrar["text"] = "Cadastrar"
        self.botaoCadastrar["font"] = ("Calibri", "8")
        self.botaoCadastrar["width"] = 12
        # self.botaoCadastrar["command"] = self.verificaSenha
        self.botaoCadastrar.pack(side="right")

        
root = Tk()
Cadastro(root)
root.mainloop()