import socket
from mappers.mapper_usuario import MapperUsuario
from  models.tipo_operacao import TipoOperacao

from models.usuario import Usuario

class Cliente:
    def __init__(self) -> None:
        self.SERVER = '127.0.0.1'
        # Porta que o Servidor esta escutando
        self.PORT = 5002
        self.tcp = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)
        self.dest = (self.SERVER, self.PORT)
      

    def criarUsuario(self,usuario:Usuario):
        self.tcp.connect(self.dest)
        dicionario: dict = MapperUsuario.usuarioToJson(usuario=usuario)
        dicionario['tipoOperacao']=TipoOperacao.criarUsuario.value
        msg=str(dicionario)
        self.tcp.send(msg.encode())
        self.tcp.close


    # def receberMensagem(self):
    #     pass
    # def enviarMensagem(self):
    #     pass
