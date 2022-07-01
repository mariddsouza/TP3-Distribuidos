import json
import socket
from typing import List
from mappers.mapper_movel import MapperMovel
from mappers.mapper_proposta import MapperProposta
from mappers.mapper_usuario import MapperUsuario
from models.movel import Movel
from models.proposta import Proposta
from models.status_resposta import StatusResposta
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
        msg=self.tcp.recv(4096)
        msg=msg.decode()
        if not msg: return StatusResposta.falha.value
        self.tcp.close()
        return int(msg)
    
    def buscarUsuario(self,cpf:int,senha:str)-> Usuario:
        
        self.tcp.connect(self.dest)
        dicionario:dict={}
        dicionario['cpf']=cpf
        dicionario['senha']=senha
        dicionario['tipoOperacao']=TipoOperacao.buscarUsuario.value
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(4096)
        if msg.decode() == " ": return None
        msg=json.loads(msg)
        self.tcp.close()
        return MapperUsuario.jsonToUsuario(dict(msg))

    def buscarMoveis(self,cpf:int)->List[Movel]:
        self.tcp.connect(self.dest)
        dicionario = {}
        dicionario['cpf']=cpf
        dicionario['tipoOperacao']=TipoOperacao.buscarMoveis.value
        msg = json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg = self.tcp.recv(4096)
        self.tcp.close()
        if not msg:
            return []
        dicionario = json.loads(msg)
        listaMoveis= []
        for k,v in dicionario.items():
            listaMoveis.append(MapperMovel.jsonToMovel(json.loads(v)))
        return listaMoveis
    

    def alterarUsuario(self,usuario:Usuario)-> None:
        self.tcp.connect(self.dest)
        dicionario: dict = MapperUsuario.usuarioToJson(usuario=usuario)
        dicionario['tipoOperacao']=TipoOperacao.alterarUsuario.value
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        self.tcp.close()
    
    def buscarTodosUsuarios(self)-> list:
        self.tcp.connect(self.dest)
        dicionario = {}
        dicionario['tipoOperacao']=TipoOperacao.buscarTodosUsuarios.value
        msg = json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg = self.tcp.recv(4096)
        if not msg: return None
        dicionario = json.loads(msg)
        listaUsuarios= []
        for k,v in dicionario.items():
            listaUsuarios.append(MapperUsuario.jsonToUsuario(json.loads(v)))
        self.tcp.close()
        return listaUsuarios

    def buscarPropostasRealizadas(self,cpf:int)->List[Proposta]:
        self.tcp.connect(self.dest)
        dicionario = {}
        dicionario['cpf']=cpf
        dicionario['tipoOperacao']=TipoOperacao.buscarPropostasRealizadas.value
        msg = json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg = self.tcp.recv(4096)
        if not msg: return None
        dicionario = json.loads(msg)
        listaPropostas= []
        for k,v in dicionario.items():
            listaPropostas.append(MapperProposta.jsonToProposta(json.loads(v)))
        self.tcp.close()
        return listaPropostas
    
    def buscarPropostasRecebidas(self,cpf:int)->List[Proposta]:
        self.tcp.connect(self.dest)
        dicionario = {}
        dicionario['cpf']=cpf
        dicionario['tipoOperacao']=TipoOperacao.buscarPropostasRecebidas.value
        msg = json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg = self.tcp.recv(4096)
        if not msg: return None
        dicionario = json.loads(msg)
        listaPropostas= []
        for k,v in dicionario.items():
            listaPropostas.append(MapperProposta.jsonToProposta(json.loads(v)))
        self.tcp.close()
        return listaPropostas
    
    def cadastrarMovel(self,cpf:int, movel:Movel)-> int:
        self.tcp.connect(self.dest)
        dicionario: dict = MapperMovel.movelToJson(movel=movel)
        dicionario['tipoOperacao']=TipoOperacao.criarMovel.value
        dicionario['cpf']=cpf
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(4096)
        msg=msg.decode()
        if not msg: return StatusResposta.falha.value
        self.tcp.close()
        return int(msg)

    def excluirMovel(self,idMovel:int,cpf:int)-> int:
        self.tcp.connect(self.dest)
        dicionario: dict = {}
        dicionario['tipoOperacao']=TipoOperacao.excluirMovel.value
        dicionario['idMovel']=idMovel
        dicionario['cpf']=cpf
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(4096 )
        msg=msg.decode()
        if not msg: return StatusResposta.falha.value
        self.tcp.close()
        return int(msg)
    
    def aceitarProposta(self,idProposta:int,cpfUsuario:int):
        self.tcp.connect(self.dest)
        dicionario: dict = {}
        dicionario['cpf']=cpfUsuario
        dicionario['tipoOperacao']=TipoOperacao.aceitarTroca.value
        dicionario['idProposta']=idProposta
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(4096)
        msg=msg.decode()
        if not msg: return StatusResposta.falha.value
        self.tcp.close()
        return int(msg)


    def recusarProposta(self,idProposta:int,cpfUsuario:int):
        self.tcp.connect(self.dest)
        dicionario: dict = {}
        dicionario['cpf']=cpfUsuario
        dicionario['tipoOperacao']=TipoOperacao.recusarTroca.value
        dicionario['idProposta']=idProposta
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(4096)
        msg=msg.decode()
        if not msg: return StatusResposta.falha.value
        self.tcp.close()
        return int(msg)
    
    def fazerProposta(self,cpfRequisitante:int,idMovelRequerido:int,idMovelProposto:int,
    cpfRequisitado:int):
        self.tcp.connect(self.dest)
        dicionario: dict = {}
        dicionario['cpfRequisitante']=cpfRequisitante
        dicionario['cpfRequisitado']=cpfRequisitado
        dicionario['idMovelProposto']=idMovelProposto
        dicionario['tipoOperacao']=TipoOperacao.proporTroca.value
        dicionario['idMovelRequerido']=idMovelRequerido
        msg=json.dumps(dicionario)
        self.tcp.send(msg.encode())
        msg=self.tcp.recv(4096)
        msg=msg.decode()
        if not msg: return StatusResposta.falha.value
        self.tcp.close()
        return int(msg)



