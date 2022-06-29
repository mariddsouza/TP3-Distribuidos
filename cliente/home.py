from cliente.cliente import Cliente
from cliente.cores import Cores
from typing import List
from models.movel import Movel
from models.proposta import Proposta

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
        print("Você possui {} móveis:".format(len(moveis)))
        for movel in moveis:
            print(cores.criarTextoEntrada("----------------------------------------"))
            print(cores.criarTextoOpcoes("ID do móvel: ")+str(movel.id))
            print(cores.criarTextoOpcoes("Nome do móvel: ")+movel.nome)
            print(cores.criarTextoOpcoes("Sobre: ")+movel.descricao)
            print(cores.criarTextoOpcoes("Tempo de uso: ")+str(movel.tempoUso))
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
        status=cliente.cadastrarMovel(cpf,movel=movel)
        print()
        print(cores.criarTextoTela("---------- FIM TELA DE CADASTRO DE MÓVEL----------"))
        print()
        return status 

    def excluirMovel():
        cores = Cores()
        cliente : Cliente = Cliente()
        print(cores.criarTextoTela("---------- TELA DE EXCLUSÃO DE MÓVEL ----------"))
        print()
        print("Insira o ID do móvel abaixo:")
        id = input(cores.criarTextoOpcoes("ID: "))
        print()
        print(cores.criarTextoTela("---------- FIM TELA DE EXCLUSÃO DE MÓVEL----------"))
        print()
        return cliente.excluirMovel(idMovel=id)
    
    def mostrarPropostasRealizadas(cpf:int):
        # cores=Cores()
        # print("Você possui os seguintes móveis:")
        # propostas=[]
        # for proposta in propostas:
        #     print(cores.criarTextoEntrada("----------------------------------------"))
        #     print(cores.criarTextoOpcoes("Móvel proposto:")+proposta.movelProposto.nome)
        #     print(cores.criarTextoOpcoes("Móvel requerido:")+proposta.movelRequerido.nome)
        #     print(cores.criarTextoOpcoes("Sobre:")+proposta.descricao)
        #     print(cores.criarTextoOpcoes("Tempo de uso:")+proposta.tempoUso)
        #     print(cores.criarTextoEntrada("----------------------------------------"))
        pass
    


