import socket
from cliente.cadastro import Cadastro
from models.movel import Movel

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
        # inserirBanco(usuario)
        return 1
    
    def criarMovel(self,cpf:int,movel:Movel )->int:
        # inserir banco de dados
        return 1

    def excluirMovel(self,cpf:int,idMovel:int )->int:
        # inserir banco de dados
        return 1

    def buscarUsuario(self,cpf:int, senha:str)->Usuario:
        # buscarBanco(cpf)
        return Usuario(nome="nome",senha="senha",cpf=123)

    def alterarUsuario(self,usuario:Usuario):
        atualizaBanco(usuario)
        pass

    def buscarTodosUsuarios()-> list:
        # Acesso ao banco    
        pass
 