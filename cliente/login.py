from tkinter import *

from sqlalchemy import null
from cliente.cliente import Cliente

from cliente.cores import Cores
from models.status_resposta import StatusResposta
from models.usuario import Usuario


class Login:
    def __init__(self,) -> None:
        pass
    def menu()->int:
        cores = Cores()
        print(cores.criarTextoTela("---------- TELA DE LOGIN ----------"))
        print()
        print("---- Bem-vindo ao Escamo ----")
        print("Escolha uma opção:")
        print(cores.criarTextoOpcoes("0")+" - Encerrar do sistema")
        print(cores.criarTextoOpcoes("1")+" - Entrar no sistema")
        print(cores.criarTextoOpcoes("2")+" - Cadastrar no sistema")
        opcao=int(input(cores.criarTextoEntrada("Opção: ")))
        print()
        return opcao

    def login()->Usuario:
        cores = Cores()
        cliente = Cliente()
        cpf=input(cores.criarTextoOpcoes("Insira seu CPF: "))
        senha=input(cores.criarTextoOpcoes("Insira sua senha: "))
        usuario=cliente.buscarUsuario(cpf=cpf,senha=senha)
        print(cores.criarTextoTela("---------- FIM TELA DE LOGIN ----------"))
        return usuario
        

        

