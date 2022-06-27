from tkinter import *
from turtle import color


class Cadastro:
    def __init__(self, master=None) -> None:
        pass
    def menu() -> int:
        print("---------- TELA DE CADASTRO ----------")
        print()
        print("Insira os seus dados abaixo:")
        nome = input("Nome:")
        cpf = input("CPF:")
        senha = input("Senha:")
        print()
        print("---------- FIM TELA DE CADASTRO ----------")
Cadastro.menu()