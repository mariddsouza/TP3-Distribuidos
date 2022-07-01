import json
import socket
from typing import List
from cliente.cadastro import Cadastro
from mappers.mapper_movel import MapperMovel
from mappers.mapper_proposta import MapperProposta
from mappers.mapper_usuario import MapperUsuario
from models.movel import Movel
from models.proposta import Proposta
from models.tipo_operacao import TipoOperacao

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
        # self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp.listen(5)
    
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
    
    def lerMensagem(self,socket)->str:
        mensagemCompleta = ""
        EOF = 0x05
        while True:
            msg = socket.recv(4096)
            if not msg: break
            if msg[len(msg) - 1] == EOF:
                mensagemCompleta += str(msg[: len(msg) - 1].decode())
                break
            else:
                mensagemCompleta+=str(msg.decode())
        return mensagemCompleta

    def enviarMensagem(self,msg:str,socket):
        EOF = 0x05
        socket.send(msg.encode())
        socket.send(bytearray([EOF]))
    
    def inicializar(self,con):
        while True:
            msg = self.lerMensagem(con)
            if not msg: break   
            dicionario= json.loads(msg)
            tipoOperacao=dicionario['tipoOperacao']
            
            if tipoOperacao==TipoOperacao.buscarUsuario.value:
                usuario = self.buscarUsuario(senha=dicionario['senha'],cpf=dicionario['cpf'])
                if usuario is not None:
                    msg =json.dumps(MapperUsuario.usuarioToJson(usuario=usuario))
                    self.enviarMensagem(msg=msg,socket=con)
                else:
                    msg=" "
                    self.enviarMensagem(msg=msg,socket=con)

            elif tipoOperacao==TipoOperacao.alterarUsuario.value:
                usuario = MapperUsuario.jsonToUsuario(dicionario) 
                self.alterarUsuario(usuario=usuario)

            elif tipoOperacao==TipoOperacao.criarUsuario.value:
                usuario = MapperUsuario.jsonToUsuario(dicionario) 
                status=self.criarUsuario(usuario=usuario)
                msg=str(status)
                self.enviarMensagem(msg=msg,socket=con)

            elif tipoOperacao == TipoOperacao.criarMovel.value:
                movel = MapperMovel.jsonToMovel(dicionario=dicionario)
                cpf=dicionario['cpf']
                status = self.criarMovel(cpf=cpf,movel = movel)
                msg=str(status)
            
                self.enviarMensagem(msg=msg,socket=con)
                
            elif tipoOperacao == TipoOperacao.excluirMovel.value:
                idMovel = dicionario['idMovel']
                cpf=dicionario['cpf']
                status = self.excluirMovel(idMovel=idMovel,cpf=cpf)
                msg = str(status)
                self.enviarMensagem(msg=msg,socket=con)

            elif tipoOperacao == TipoOperacao.buscarTodosUsuarios.value:
                listaUsuarios = self.buscarTodosUsuarios()
                dicionario={}
                cont=0
                while(cont!=len(listaUsuarios)):
                    dicionario[str(cont)]=json.dumps(MapperUsuario.usuarioToJson(usuario=listaUsuarios[cont]))
                    cont+=1
                msg =json.dumps(dicionario)
                self.enviarMensagem(msg=msg,socket=con)

            elif tipoOperacao==TipoOperacao.buscarMoveis.value:
                listaMoveis = self.buscarMoveis(dicionario['cpf'])
                dicionario={}
                cont=0
                while(cont!=len(listaMoveis)):
                    dicionario[str(cont)]=json.dumps(MapperMovel.movelToJson(movel=listaMoveis[cont]))
                    cont+=1
                msg =json.dumps(dicionario)
                self.enviarMensagem(msg=msg,socket=con)
            
            elif tipoOperacao == TipoOperacao.buscarPropostasRealizadas.value:
                cpf=dicionario['cpf']
                listaPropostas = self.buscarPropostasRealizadas(cpf=cpf)
                dicionario={}
                cont=0
                while(cont!=len(listaPropostas)):
                    dicionario[str(cont)]=json.dumps(MapperProposta.propostaToJson(proposta=listaPropostas[cont]))
                    cont+=1
                msg =json.dumps(dicionario)
                self.enviarMensagem(msg=msg,socket=con)
            
            elif tipoOperacao == TipoOperacao.buscarPropostasRecebidas.value:
                cpf=dicionario['cpf']
                listaPropostas = self.buscarPropostasRecebidas(cpf=cpf)
                dicionario={}
                cont=0
                while(cont!=len(listaPropostas)):
                    dicionario[str(cont)]=json.dumps(MapperProposta.propostaToJson(proposta=listaPropostas[cont]))
                    cont+=1
                msg =json.dumps(dicionario)
                self.enviarMensagem(msg=msg,socket=con)

            elif tipoOperacao == TipoOperacao.aceitarTroca.value: 
                cpf=dicionario['cpf']
                idProposta = dicionario['idProposta']
                status=self.aceitarProposta(idProposta=idProposta,cpfUsuarioAlvo=cpf)
                msg=str(status)
                self.enviarMensagem(msg=msg,socket=con)

            elif tipoOperacao == TipoOperacao.recusarTroca.value:
                cpf=dicionario['cpf']
                idProposta = dicionario['idProposta']
                status=self.recusarProposta(idProposta=idProposta,cpfUsuarioAlvo=cpf)
                msg=str(status)
                self.enviarMensagem(msg=msg,socket=con)

            elif tipoOperacao == TipoOperacao.proporTroca.value:
                cpfRequisitante=dicionario['cpfRequisitante']
                cpfRequisitado=dicionario['cpfRequisitado']
                idMovelProposto=dicionario['idMovelProposto']
                idMovelRequerido=dicionario['idMovelRequerido']
                status=self.fazerProposta(idMovelRequerido,idMovelProposto,cpfRequisitante,cpfRequisitado)
                msg=str(status)
                self.enviarMensagem(msg=msg,socket=con)