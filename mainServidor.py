#Servidor TCP
import json
from mailbox import NotEmptyError
import socket
from mappers.mapper_usuario import MapperUsuario

from models.tipo_operacao import TipoOperacao
from models.usuario import Endereco, Usuario
from servidor.servidor import Servidor
# Endereco IP do Servidor
# endereco:Endereco= Endereco(rua="Rua A",bairro="Vila Operária",cep="39100-000",numero=35)
# usuario:Usuario=Usuario(nome="Fabio",cpf=10656980621,endereco=endereco,email="email@email.com",
# moveis=[],senha="senha",telefone="(38)988337225",propostasFeitas=[],propostasRecebidas=[])
servidor: Servidor = Servidor()
# listaUsuarios = [usuario,usuario]

while True:
    con, cliente = servidor.tcp.accept()
    print ('Concetado por ', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        dicionario= json.loads(msg)
        tipoOperacao=dicionario['tipoOperacao']
        if tipoOperacao==TipoOperacao.buscarUsuario.value:
            usuario = servidor.buscarUsuario(senha=dicionario['senha'],cpf=dicionario['cpf'])
            msg =json.dumps(MapperUsuario.usuarioToJson(usuario=usuario))
            con.send(msg.encode())

        elif tipoOperacao==TipoOperacao.alterarUsuario.value:
            usuario = json.loads(MapperUsuario.jsonToUsuario(dicionario=dicionario))
            servidor.alterarUsuario(usuario=usuario)

        elif tipoOperacao==TipoOperacao.criarUsuario.value:
            usuario = json.loads(MapperUsuario.jsonToUsuario(dicionario=dicionario))
            servidor.criarUsuario(usuario=usuario)

        elif tipoOperacao == TipoOperacao.buscarTodosUsuarios.value:
            listaUsuarios = servidor.buscarTodosUsuarios()
            dicionario={}
            cont=0
            while(cont!=len(listaUsuarios)):
                dicionario[str(cont)]=json.dumps(MapperUsuario.usuarioToJson(usuario=listaUsuarios[cont]))
                cont+=1
            msg =json.dumps(dicionario)
            con.send(msg.encode())

        elif tipoOperacao==TipoOperacao.proporTroca:
            pass

        elif tipoOperacao == TipoOperacao.aceitarTroca:
            pass

        elif tipoOperacao == TipoOperacao.recusarTroca:
            pass
        
    print ('Finalizando conexao do cliente', cliente)
    con.close()


