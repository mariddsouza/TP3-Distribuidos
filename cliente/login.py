from tkinter import *
class Login:
    def __init__(self,master=None) -> None:
        pass
    def menu()->int:
        print("---------- TELA DE LOGIN ----------")
        print()
        print("---- Bem-vindo ao Escamo ----")
        print("Escolha uma opção:")
        print("1 - Entrar no sistema")
        print("2 - Cadastrar no sistema")
        opcao=int(input("Opção:"))
        print()
        print("---------- FIM TELA DE LOGIN ----------")
        return opcao
Login.menu()