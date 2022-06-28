from cliente.cliente import Cliente
from cliente.cores import Cores
from typing import List
from models.movel import Movel

class Home:
    def __init__(self) -> None:
        pass
    def menu()-> int:
        cores = Cores()
        print(cores.criarTextoTela("---------- TELA INICIAL ----------"))
        print()
        print("Escolha uma opção:")
        print(cores.criarTextoOpcoes("0")+" - Logout")
        print(cores.criarTextoOpcoes("1")+" - Ver meus móveis")
        print(cores.criarTextoOpcoes("2")+" - Cadastrar móvel")
        print(cores.criarTextoOpcoes("3")+" - Excluir móvel")
        print(cores.criarTextoOpcoes("4")+" - Ver propostas realizadas")
        print(cores.criarTextoOpcoes("5")+" - Ver propostas recebidas")
        print(cores.criarTextoOpcoes("6")+" - Ver móveis disponíveis para escambo")
        opcao=int(input(cores.criarTextoEntrada("Opção: ")))
        print()
        return opcao

    def mostrarMoveis(moveis:List[Movel]):
        cores=Cores()
        print("Você possui os seguintes móveis:")
        for movel in moveis:
            print(cores.criarTextoEntrada("----------------------------------------"))
            print(cores.criarTextoOpcoes("ID do móvel:")+movel.id)
            print(cores.criarTextoOpcoes("Nome do móvel:")+movel.nome)
            print(cores.criarTextoOpcoes("Sobre:")+movel.descricao)
            print(cores.criarTextoOpcoes("Tempo de uso:")+movel.tempoUso)
            print(cores.criarTextoEntrada("----------------------------------------"))
    
    def cadastrarMovel(cpf:int):
        cores = Cores()
        cliente : Cliente = Cliente()
        print(cores.criarTextoTela("---------- TELA DE CADASTRO DE MÓVEL ----------"))
        print()
        print("Insira os dados do seu móvel abaixo:")
        nome = input(cores.criarTextoOpcoes("Nome: "))
        descricao = input(cores.criarTextoOpcoes("Descrição: "))
        tempoUso = int(input(cores.criarTextoOpcoes("Tempo de uso: ")))
        movel = Movel(nome=nome,tempoUso=tempoUso,descricao=descricao)
        print()
        print(cores.criarTextoTela("---------- FIM TELA DE CADASTRO DE MÓVEL----------"))
        print()
        return cliente.cadastrarMovel(cpf,movel=movel)


