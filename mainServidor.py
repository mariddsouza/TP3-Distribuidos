#Servidor TCP
import json
from mailbox import NotEmptyError
from mappers.mapper_movel import MapperMovel
from mappers.mapper_proposta import MapperProposta
from mappers.mapper_usuario import MapperUsuario

from models.tipo_operacao import TipoOperacao
from models.usuario import Usuario
from servidor.servidor import Servidor

servidor: Servidor = Servidor()

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
            print("TipoOperacao")
            movel = MapperMovel.jsonToMovel(dicionario=dicionario)
            cpf=dicionario['cpf']
            status = servidor.criarMovel(cpf=cpf,movel = movel)
            msg=str(status)
           
            con.send(msg.encode())
            
        elif tipoOperacao == TipoOperacao.excluirMovel.value:
            idMovel = dicionario['idMovel']
            cpf=dicionario['cpf']
            status = servidor.excluirMovel(idMovel=idMovel,cpf=cpf)
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
            dicionario={}
            cont=0
            while(cont!=len(listaMoveis)):
                dicionario[str(cont)]=json.dumps(MapperMovel.movelToJson(movel=listaMoveis[cont]))
                cont+=1
            msg =json.dumps(dicionario)
            con.send(msg.encode())
        
        elif tipoOperacao == TipoOperacao.buscarPropostasRealizadas.value:
            # print("Entrei")
            cpf=dicionario['cpf']
            listaPropostas = servidor.buscarPropostasRealizadas(cpf=cpf)
            # print("Lista propostas: ",listaPropostas)
            dicionario={}
            cont=0
            while(cont!=len(listaPropostas)):
                dicionario[str(cont)]=json.dumps(MapperProposta.propostaToJson(proposta=listaPropostas[cont]))
                cont+=1
            msg =json.dumps(dicionario)
            con.send(msg.encode())
        
        elif tipoOperacao == TipoOperacao.buscarPropostasRecebidas.value:
            # print("Entrei")
            cpf=dicionario['cpf']
            listaPropostas = servidor.buscarPropostasRecebidas(cpf=cpf)
            # print("Lista propostas: ",listaPropostas)
            dicionario={}
            cont=0
            while(cont!=len(listaPropostas)):
                dicionario[str(cont)]=json.dumps(MapperProposta.propostaToJson(proposta=listaPropostas[cont]))
                cont+=1
            msg =json.dumps(dicionario)
            con.send(msg.encode())

        elif tipoOperacao == TipoOperacao.aceitarTroca.value: 
            cpf=dicionario['cpf']
            idProposta = dicionario['idProposta']
            status=servidor.aceitarProposta(idProposta=idProposta,cpfUsuarioAlvo=cpf)
            msg=str(status)
            con.send(msg.encode())

        elif tipoOperacao == TipoOperacao.recusarTroca.value:
            cpf=dicionario['cpf']
            idProposta = dicionario['idProposta']
            status=servidor.recusarProposta(idProposta=idProposta,cpfUsuarioAlvo=cpf)
            msg=str(status)
            print(msg)
            con.send(msg.encode())
        elif tipoOperacao == TipoOperacao.proporTroca.value:
            cpfRequisitante=dicionario['cpfRequisitante']
            cpfRequisitado=dicionario['cpfRequisitado']
            idMovelProposto=dicionario['idMovelProposto']
            idMovelRequerido=dicionario['idMovelRequerido']
            status=servidor.fazerProposta(idMovelRequerido,idMovelProposto,cpfRequisitante,cpfRequisitado)
            msg=str(status)
            print(msg)
            con.send(msg.encode())
    # con.close()
    print ('Finalizando conexão do cliente', cliente)
    


