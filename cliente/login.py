from tkinter import *

from cliente.cores import Cores


class Login:
    def __init__(self,) -> None:
        pass
    def menu()->int:
        cores = Cores()
        print(cores.criarTextoTela("---------- TELA DE LOGIN ----------"))
        print()
        print("---- Bem-vindo ao Escamo ----")
        print("Escolha uma opção:")
        print(cores.criarTextoOpcoes("0")+" - Fechar do sistema")
        print(cores.criarTextoOpcoes("1")+" - Entrar no sistema")
        print(cores.criarTextoOpcoes("2")+" - Cadastrar no sistema")
        opcao=int(input(cores.criarTextoEntrada("Opção: ")))
        print()
        print(cores.criarTextoTela("---------- FIM TELA DE LOGIN ----------"))
        print()
        return opcao
