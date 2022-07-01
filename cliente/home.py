from cliente.cliente import Cliente
from cliente.cores import Cores
from typing import List
from models.movel import Movel
from models.proposta import Proposta, StatusProposta
from models.status_resposta import StatusResposta
from models.usuario import Usuario

class Home:
    def __init__(self,) -> None:
        pass
    def menu(self)-> int:
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
        print(cores.criarTextoOpcoes("6")+" - Aceitar uma proposta")
        print(cores.criarTextoOpcoes("7")+" - Rejeitar uma proposta")
        print(cores.criarTextoOpcoes("8")+" - Ver móveis disponíveis para escambo")
        print(cores.criarTextoOpcoes("9")+" - Fazer uma proposta")
        opcao=int(input(cores.criarTextoEntrada("Opção: ")))
        print()
        return opcao

    def mostrarMoveis(self,moveis:List[Movel]):
        cores=Cores()
        print("Você possui os seguintes móveis:")
        for movel in moveis:
            print(cores.criarTextoEntrada("----------------------------------------"))
            print(cores.criarTextoOpcoes("ID do móvel: ")+str(movel.id))
            print(cores.criarTextoOpcoes("Nome do móvel: ")+movel.nome)
            print(cores.criarTextoOpcoes("Sobre: ")+movel.descricao)
            print(cores.criarTextoOpcoes("Tempo de uso: ")+str(movel.tempoUso)+ " anos.")
            print(cores.criarTextoEntrada("----------------------------------------"))
        print("Quantidade de móveis que você possui: {}".format(len(moveis)))
        print(cores.criarTextoEntrada("----------------------------------------"))
        print()
    
    def cadastrarMovel(self,cpf:int):
        cores = Cores()
        cliente: Cliente=Cliente()
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

    def excluirMovel(self,cpf:int):
        cliente: Cliente=Cliente()
        cores = Cores()
        print(cores.criarTextoTela("---------- TELA DE EXCLUSÃO DE MÓVEL ----------"))
        print()
        print("Insira o ID do móvel abaixo:")
        id = input(cores.criarTextoOpcoes("ID do móvel: "))
        print()
        print(cores.criarTextoTela("---------- FIM TELA DE EXCLUSÃO DE MÓVEL----------"))
        print()
        return cliente.excluirMovel(idMovel=id,cpf=cpf)
    
    def mostrarPropostasRealizadas(self,propostas:List[Proposta]):
        cores=Cores()
        print("Você fez as seguintes propostas:")
        for proposta in propostas:
            print(cores.criarTextoEntrada("----------------------------------------"))
            print(cores.criarTextoOpcoes("Móvel proposto: ")+proposta.movelProposto.nome)
            print(cores.criarTextoOpcoes("Móvel requerido: ")+proposta.movelRequerido.nome)
            print(cores.criarTextoOpcoes("Usuário requisitado: ")+proposta.usuarioAlvo.nome)
            status=proposta.status
            if status == StatusProposta.EmEspera.value:
                msg = "Esperando resposta do proprietário."
            elif status == StatusProposta.Aceito.value:
                msg = "Proprietário aceitou a troca."
            else:
                msg = "Proprietário recusou a troca."
            print(cores.criarTextoOpcoes("Status: ")+msg)
            print(cores.criarTextoEntrada("----------------------------------------"))
        print("Quantidade de propostas que você fez: {}".format(len(propostas)))
        print(cores.criarTextoEntrada("----------------------------------------"))
        print()
    
    def mostrarPropostasRecebidas(self,propostas:List[Proposta]):
        cores=Cores()
        print("Você recebeu as seguintes propostas:")
        for proposta in propostas:
            print(cores.criarTextoEntrada("----------------------------------------"))
            print(cores.criarTextoEntrada("ID proposta: ")+str(proposta.idProposta))
            print(cores.criarTextoOpcoes("Móvel proposto: ")+proposta.movelProposto.nome)
            print(cores.criarTextoOpcoes("Móvel requerido: ")+proposta.movelRequerido.nome)
            print(cores.criarTextoOpcoes("Usuário requisitante: ")+proposta.usuarioRequisitante.nome)
            status=proposta.status
            if status == StatusProposta.EmEspera.value:
                msg = "Esperando sua resposta."
            elif status == StatusProposta.Aceito.value:
                msg = "Você aceitou a troca."
            else:
                msg = "Você recusou a troca."
            print(cores.criarTextoOpcoes("Status: ")+msg)
            print(cores.criarTextoEntrada("----------------------------------------"))
        print("Quantidade de propostas que você recebeu: {}".format(len(propostas)))
        print(cores.criarTextoEntrada("----------------------------------------"))
        print()
    
    def aceitarProposta(self,cpfUsuario:int):
        cores = Cores()
        cliente: Cliente=Cliente()
        print()
        print("Insira o ID da proposta abaixo:")
        id = input(cores.criarTextoOpcoes("ID da proposta: "))
        print()
        cliente.aceitarProposta(cpfUsuario=cpfUsuario,idProposta=id)
    
    def recusarProposta(self,cpfUsuario:int):
        cores = Cores()
        cliente: Cliente=Cliente()
        print()
        print("Insira o ID da proposta abaixo:")
        id = input(cores.criarTextoOpcoes("ID da proposta: "))
        print()
        cliente.recusarProposta(cpfUsuario=cpfUsuario,idProposta=id)

    def mostrarMoveisDisponiveisEscambo(self,usuarios:List[Usuario],cpf:int):
        cores = Cores()
        contador=0
        for usuario in usuarios:
            if usuario.cpf!=cpf:
                print(cores.criarTextoTela("----------------------------------------"))
                print(cores.criarTextoEntrada("ID usuário: ")+str(contador))
                print(cores.criarTextoOpcoes("Nome do proprietário: ")+usuario.nome)
                print("{} possui os seguintes móveis:".format(usuario.nome))
                for movel in usuario.moveis:
                    print(cores.criarTextoEntrada("----------------------------------------"))
                    print(cores.criarTextoOpcoes("ID do móvel: ")+str(movel.id))
                    print(cores.criarTextoOpcoes("Nome do móvel: ")+movel.nome)
                    print(cores.criarTextoOpcoes("Sobre: ")+movel.descricao)
                    print(cores.criarTextoOpcoes("Tempo de uso: ")+str(movel.tempoUso)+ " anos.")
                    print(cores.criarTextoEntrada("----------------------------------------"))
                print(cores.criarTextoTela("----------------------------------------"))
            contador+=1

    def fazerProposta(self,cpfRequisitante:int,usuarios:List[Usuario]):
        cliente:Cliente=Cliente()
        cores:Cores=Cores()
        print(cores.criarTextoOpcoes("Preencha corretamente as entradas abaixo"))
        idMovelRequerido=int(input(cores.criarTextoOpcoes("ID do móvel quer você quer: ")))
        idMovelProposto=int(input(cores.criarTextoOpcoes("ID do móvel que você quer propor: ")))
        cpfRequisitado=int(input(cores.criarTextoOpcoes("ID do proprietário: ")))
        cpfRequisitado = usuarios[cpfRequisitado].cpf
        
        cliente.fazerProposta(cpfRequisitante,idMovelRequerido,idMovelProposto,cpfRequisitado)
       


        
        
    


