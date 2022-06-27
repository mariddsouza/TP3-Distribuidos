from tkinter import *
class Login:
    def __init__(self,master=None) -> None:
        self.fontePadrao=("Arial","10")

        self.containerCpf =Frame(master)
        self.containerCpf["padx"] = 20
        self.containerCpf.pack()
        self.cpfLabel = Label(self.containerCpf,text="CPF   ", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)
        self.cpf= Entry(self.containerCpf)
        self.cpf["font"]=self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.containerSenha = Frame(master)
        self.containerSenha["pady"] = 10
        self.containerSenha.pack()
        self.senhaLabel = Label(self.containerSenha,text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha= Entry(self.containerSenha)
        self.senha["font"]=self.fontePadrao
        self.senha.pack(side=LEFT)
        self.senha["show"] = "*"

        self.containerBotao = Frame(master)
        self.containerBotao.pack()
        self.botaoEntrar = Button(self.containerBotao)
        self.botaoEntrar["text"] = "Entrar"
        self.botaoEntrar["font"] = ("Calibri", "8")
        self.botaoEntrar["width"] = 12
        # self.botaoEntrar["command"] = self.verificaSenha
        self.botaoEntrar.pack(side="right")

        self.botaoCadastrar = Button(self.containerBotao)
        self.botaoCadastrar["text"] = "Cadastrar"
        self.botaoCadastrar["font"] = ("Calibri", "8")
        self.botaoCadastrar["width"] = 12
        # self.botaoCadastrar["command"] = self.verificaSenha
        self.botaoCadastrar.pack(side="right")

root = Tk()
Login(root)
root.mainloop()