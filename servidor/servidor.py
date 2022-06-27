import socket

from models.usuario import Usuario


class Servidor:
    def __init__(self) -> None:
        self.HOST = ''
    # Porta que o Servidor vai escutar
        self.PORT = 5002
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.orig = (self.HOST, self.PORT)
        self.tcp.bind(self.orig)
        self.tcp.listen(1)
    
    def criarUsuario(self,usuario:Usuario )->None:
        # Acesso ao banco
        pass   
    def buscarUsuario(self,cpf:int, senha:str)->Usuario:
        # Acesso ao banco
        pass
    def alterarUsuario(self,usuario:Usuario):
        # Acesso ao banco
        pass
    def buscarTodosUsuarios()-> list:
        # Acesso ao banco    
        pass
 