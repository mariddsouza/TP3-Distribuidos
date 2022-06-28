import socket
from typing import List
from cliente.cadastro import Cadastro
from models.movel import Movel
from models.proposta import Proposta

from models.usuario import Usuario
from banco.cadastro import inserirBanco
from banco.cadastro import buscarBanco
from banco.cadastro import atualizaBanco

class Servidor:
    def __init__(self) -> None:
        self.HOST = ''
    # Porta que o Servidor vai escutar
        self.PORT = 5002
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.orig = (self.HOST, self.PORT)
        self.tcp.bind(self.orig)
        self.tcp.listen(1)
    
    def criarUsuario(self,usuario:Usuario )->int:
        return inserirBanco(usuario)
    
    def criarMovel(self,cpf:int,movel:Movel )->int:
        # inserir banco de dados
        return 1

    def excluirMovel(self,cpf:int,idMovel:int )->int:
        # inserir banco de dados
        return 1

    def buscarUsuario(self,cpf:int, senha:str)->Usuario:
        buscarBanco(cpf)
        return Usuario(nome="nome",senha="senha",cpf=123)

    # def alterarUsuario(self,usuario:Usuario):
    #     atualizaBanco(usuario)
    #     pass

    def buscarTodosUsuarios()-> List[Usuario]:
        # Acesso ao banco    
        pass
    def buscarPropostasRealizadas(cpf:int)-> List[Proposta]:
        # Buscar no banco as propostas realizadas a partir de um cpf
        pass
    def buscarPropostasRecebidas(cpf:int)-> List[Proposta]:
        # Buscar no banco as propostas recebidas a partir de um cpf
        pass
    def buscarMovel(idMovel:int)->Movel:
        # Buscar no banco as propostas recebidas a partir de um id
        pass
    def aceitarProposta():
        # Aceita uma proposta a partir do ID da proposta
        pass
    def recusarProposta():
         # Recusa uma proposta a partir do ID da proposta
        pass
    def fazerProposta():
        # Cria uma proposta de forma a naloga a criar usuario
        pass
 