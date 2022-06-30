import socket
from typing import List
from cliente.cadastro import Cadastro
from models.movel import Movel
from models.proposta import Proposta

from models.usuario import Usuario
from banco.cadastro import aceitaProposta, buscarMoveis, deletarMovel, inserirUsuario, inserirMovel
from banco.cadastro import buscarUsuarioBanco
from banco.cadastro import atualizaBanco
from banco.cadastro import listarUsuarios
from banco.cadastro import criarProposta
from banco.cadastro import buscaMovel
from banco.cadastro import buscaPropostaRealizada
from banco.cadastro import buscaPropostaRecebida
from banco.cadastro import recusaProposta

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
        return inserirUsuario(usuario)
    
    def criarMovel(self,cpf:int,movel:Movel )->int:
        return inserirMovel(cpf, movel)

    def excluirMovel(self,idMovel:int ,cpf:int)->int:
       return deletarMovel(idMovel,cpf=cpf)

    def buscarUsuario(self,cpf:int, senha:str)->Usuario:
        return buscarUsuarioBanco(cpf=cpf,senha=senha)
    
    def buscarMoveis(self,cpf:str):
        return buscarMoveis(cpf=cpf)

    def alterarUsuario(self,usuario:Usuario):
        atualizaBanco(usuario)
      
    def buscarTodosUsuarios(self)-> List[Usuario]:
        return listarUsuarios()

    def buscarMovel(self,idMovel:int)->Movel:
        return buscaMovel(idMovel)

    def fazerProposta(self,idMovelRequerido: int, idMovelProposto: int, cpfUsuarioRequisitante:str, cpfUsuarioAlvo:str):
        return criarProposta(idMovelRequerido, idMovelProposto, cpfUsuarioRequisitante, cpfUsuarioAlvo)

    def buscarPropostasRealizadas(self,cpf:int)-> List[Proposta]: 
        return buscaPropostaRealizada(cpf)

    def buscarPropostasRecebidas(self,cpf:int)-> List[Proposta]:
        return buscaPropostaRecebida(cpf)
        
    
    def aceitarProposta(self,idProposta:int,cpfUsuarioAlvo:int)-> int:
        return aceitaProposta(idProposta,cpfUsuarioAlvo=cpfUsuarioAlvo)
        
    def recusarProposta(self,idProposta:int,cpfUsuarioAlvo:int)->int:
        return recusaProposta(idProposta,cpfUsuarioAlvo=cpfUsuarioAlvo)
    