import json
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
      

    def criarUsuario(self,usuario:Usuario)-> int:
        self.tcp.connect(self.dest)
        dicionario: dict = MapperUsuario.usuarioToJson(usuario=usuario)
        dicionario['tipoOperacao']=TipoOperacao.criarUsuario.value
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(1024)
        msg=msg.decode()
        if not msg: return False
        self.tcp.close
        return int(msg)
    
    def buscarUsuario(self,cpf:int,senha:str)-> Usuario:
        self.tcp.connect(self.dest)
        dicionario:dict={}
        dicionario['cpf']=cpf
        dicionario['senha']=senha
        dicionario['tipoOperaçao']=TipoOperacao.buscarUsuario.value
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(1024)
        if not msg: return None
        msg=json.loads(msg)
        self.tcp.close
        return MapperUsuario.jsonToUsuario(dict(msg))

    def alterarUsuario(self,usuario:Usuario)-> None:
        self.tcp.connect(self.dest)
        dicionario: dict = MapperUsuario.usuarioToJson(usuario=usuario)
        dicionario['tipoOperacao']=TipoOperacao.alterarUsuario.value
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        self.tcp.close
    
    def buscarTodosUsuarios(self)-> list:
        self.tcp.connect(self.dest)
        dicionario = {}
        dicionario['tipoOperacao']=TipoOperacao.buscarTodosUsuarios.value
        msg = json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg = self.tcp.recv(1024)
        if not msg: return None
        dicionario = json.loads(msg)
        print(dicionario)
        listaUsuarios= []
        for k,v in dicionario.items():
            listaUsuarios.append(MapperUsuario.jsonToUsuario(json.loads(v)))
        self.tcp.close
        return listaUsuarios


