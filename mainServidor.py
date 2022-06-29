#Servidor TCP
import json
from mailbox import NotEmptyError
import socket
from mappers.mapper_movel import MapperMovel
from mappers.mapper_usuario import MapperUsuario

from models.tipo_operacao import TipoOperacao
from models.usuario import Usuario
from servidor.servidor import Servidor
# Endereco IP do Servidor
# endereco:Endereco= Endereco(rua="Rua A",bairro="Vila Operária",cep="39100-000",numero=35)
# usuario:Usuario=Usuario(nome="Fabio",cpf=10656980621,endereco=endereco,email="email@email.com",
# moveis=[],senha="senha",telefone="(38)988337225",propostasFeitas=[],propostasRecebidas=[])
servidor: Servidor = Servidor()
# listaUsuarios = [usuario,usuario]

while True:
    con, cliente = servidor.tcp.accept()
    print ('Conectado por ', cliente)
    while True:
        msg = con.recv(4096)
        if not msg: break
        dicionario= json.loads(msg)
        tipoOperacao=dicionario['tipoOperacao']

        if tipoOperacao==TipoOperacao.buscarUsuario.value:
            usuario = servidor.buscarUsuario(senha=dicionario['senha'],cpf=dicionario['cpf'])
            if usuario is not None:
                # print("Entrei")
                msg =json.dumps(MapperUsuario.usuarioToJson(usuario=usuario))
                con.send(msg.encode())
            else:
                con.send(" ".encode())

        elif tipoOperacao==TipoOperacao.alterarUsuario.value:
            usuario = MapperUsuario.jsonToUsuario(dicionario) 
            servidor.alterarUsuario(usuario=usuario)

        elif tipoOperacao==TipoOperacao.criarUsuario.value:
            usuario = MapperUsuario.jsonToUsuario(dicionario) 
            status=servidor.criarUsuario(usuario=usuario)
            msg=str(status)
            con.send(msg.encode())

        elif tipoOperacao == TipoOperacao.criarMovel.value:
            movel = MapperMovel.jsonToMovel(dicionario=dicionario)
            cpf=dicionario['cpf']
            status = servidor.criarMovel(cpf=cpf,movel = movel)
            msg=str(status)
            con.send(msg.encode())
            
        elif tipoOperacao == TipoOperacao.excluirMovel.value:
            cpf = str(dicionario['cpf'])
            idMovel = dicionario['idMovel']
            status = servidor.excluirMovel(cpf=cpf,idMovel=idMovel)
            msg = str(status)
            con.send(msg.encode())

        elif tipoOperacao == TipoOperacao.buscarTodosUsuarios.value:
            listaUsuarios = servidor.buscarTodosUsuarios()
            dicionario={}
            cont=0
            while(cont!=len(listaUsuarios)):
                dicionario[str(cont)]=json.dumps(MapperUsuario.usuarioToJson(usuario=listaUsuarios[cont]))
                cont+=1
            msg =json.dumps(dicionario)
            con.send(msg.encode())

        elif tipoOperacao==TipoOperacao.buscarMoveis.value:
            listaMoveis = servidor.buscarMoveis(dicionario['cpf'])
            print(listaMoveis)
            dicionario={}
            cont=0
            while(cont!=len(listaMoveis)):
                dicionario[str(cont)]=json.dumps(MapperMovel.movelToJson(movel=listaMoveis[cont]))
                cont+=1
            msg =json.dumps(dicionario)
            con.send(msg.encode())
            pass

        elif tipoOperacao == TipoOperacao.aceitarTroca:
            pass

        elif tipoOperacao == TipoOperacao.recusarTroca:
            pass
        
        
    print ('Finalizando conexão do cliente', cliente)
    con.close()


