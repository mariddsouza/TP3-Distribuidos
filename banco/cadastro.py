from logging import Logger
import sqlite3
import sys
import os

from sqlite3 import Error
from typing import List
from unittest import result

#from sqlalchemy import false
from models.status_resposta import StatusResposta
sys.path.append(os.path.abspath('./'))
from models.usuario import Usuario
from models.movel import Movel
from models.proposta import Proposta

def criarBanco():
    cursor = sqlite3.connect("UserCadastro.bd").cursor()
    sql_file = open("banco/criarBanco.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
    cursor.close()


def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect('UserCadastro.bd',check_same_thread=False)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()


def ExecutaSQL(conexao,sql): 
    try:
        c=conexao.cursor()
        var=c.execute(sql)
        conexao.commit()
        return var
    except Error as ex:
        print(ex)


def inserirUsuario(user:Usuario)->int:
    try:
        nome=user.nome
        senha=user.senha
        cpf=str(user.cpf)
        vsql="SELECT * FROM Usuario WHERE cpf == {}".format(cpf)
        result = ExecutaSQL(vcon,vsql).fetchone()
        if(result==None):
            vsql="INSERT INTO Usuario(nome,senha,cpf)VALUES('"+nome+"','"+senha+"','"+cpf+"')"
            ExecutaSQL(vcon,vsql)
            return StatusResposta.sucesso.value
        else:
            return StatusResposta.falha.value 
    except :
        return StatusResposta.falha.value 
       
def inserirMovel(cpf:str, movel:Movel):
    try:
        nome=movel.nome
        tempoUso=movel.tempoUso
        descricao=movel.descricao
        vsql="INSERT INTO Movel(nome,tempoUso,descricao,Usuario_cpf) VALUES('"+nome+"','"+str(tempoUso)+"','"+descricao+"','"+str(cpf)+"');"
        ExecutaSQL(vcon,vsql)
        return  StatusResposta.sucesso.value
    except Error:
        return StatusResposta.falha.value



def deletarMovel(idMovel:int,cpf:int):
    try:
        vsql="DELETE FROM Movel WHERE idMovel == '"+str(idMovel)+"' AND Usuario_cpf == '"+str(cpf)+"';"
        ExecutaSQL(vcon,vsql)
        return StatusResposta.sucesso.value
    except:
        return StatusResposta.falha.value

def buscarUsuarioBanco(cpf:str,senha:str)->Usuario:
    vsql="SELECT * FROM Usuario WHERE cpf =='"+cpf+"' AND senha == '"+senha+"';"
    result=ExecutaSQL(vcon,vsql).fetchone()
    if result == None:
        return None
    else:
        return Usuario(nome=result[1],senha=result[2],cpf=int(result[0]))

def buscarUsuarioBancoCpf(cpf:str)->Usuario:
    vsql="SELECT * FROM Usuario WHERE cpf =='"+cpf+"';"
    result=ExecutaSQL(vcon,vsql).fetchone()
    
    if result == None:
        return None
    else:
        return Usuario(nome=result[1],senha=result[2],cpf=int(result[0]))


def atualizaBanco(user:Usuario):
    nome=user.nome
    senha=user.senha
    cpf=str(user.cpf)
    vsql="UPDATE Usuario SET cpf == '"+cpf+"', nome == '"+nome+"', senha == '"+senha+"' WHERE cpf= '"+cpf+"';"
    ExecutaSQL(vcon,vsql)


def listarUsuarios()-> List[Usuario]:
    vsql="SELECT * FROM Usuario ;"
    usuarios = []
    result = ExecutaSQL(vcon,vsql).fetchall()
    for usuario in result:
        cpf=int(usuario[0])
        usuarios.append( Usuario(nome=usuario[1],senha=usuario[2],cpf=cpf,))
    return usuarios
 
def buscarMoveis(cpf)-> List[Movel]:
    moveis = []
    vsql="SELECT * FROM Movel WHERE Usuario_cpf == "+str(cpf)+";"
    result = ExecutaSQL(vcon,vsql).fetchall()
    for movel in result:
        moveis.append( Movel(id=movel[0],nome=movel[1],descricao=movel[3],tempoUso=movel[2]))
    return moveis


def criarProposta(idMovelRequirido: int, idMovelProposto: int, cpfUsuarioRequisitante:str, cpfUsuarioAlvo:str):
    try:
        vsql="INSERT INTO Proposta(usuarioRequisitante, usuarioAlvo, moveisPropostos, moveisRequiridos, status)VALUES('"+str(cpfUsuarioRequisitante)+"','"+str(cpfUsuarioAlvo)+"','"+str(idMovelProposto)+"','"+str(idMovelRequirido)+"',0)"
        ExecutaSQL(vcon,vsql)
        return StatusResposta.sucesso.value
    except Error:
        return StatusResposta.falha.value
def buscaMovel(idMovel:int):
    vsql="SELECT * FROM Movel WHERE idMovel == '"+str(idMovel)+"'; "
    querry= ExecutaSQL(vcon,vsql).fetchone()
    return Movel(querry[1],querry[2],querry[3],querry[0])

def buscaPropostaRealizada(cpf:int)->List[Proposta]:
    propostas=[]
    vsql="SELECT * FROM Proposta WHERE usuarioRequisitante == '"+str(cpf)+"';"
    result= ExecutaSQL(vcon,vsql).fetchall()
    for proposta in result:
        usuarioRequisitante = buscarUsuarioBancoCpf(proposta[0])
        usuarioRequisitado = buscarUsuarioBancoCpf(proposta[1])
        movelProposto = buscaMovel(proposta[2])
        movelRequisitado = buscaMovel(proposta[3])
        status=proposta[4]
        idProposta=proposta[5]
        propostas.append( Proposta(usuarioAlvo=usuarioRequisitado,usuarioRequisitante=usuarioRequisitante,
        idProposta=idProposta,movelProposto=movelProposto,movelRequerido=movelRequisitado,status=status))
    return propostas

def buscaPropostaRecebida(cpf:int):
    propostas=[]
    vsql="SELECT * FROM Proposta WHERE usuarioAlvo == '"+str(cpf)+"'; "
    result= ExecutaSQL(vcon,vsql).fetchall()
    for proposta in result:
        usuarioRequisitante = buscarUsuarioBancoCpf(proposta[0])
        usuarioRequisitado = buscarUsuarioBancoCpf(proposta[1])
        movelProposto = buscaMovel(proposta[2])
        movelRequisitado = buscaMovel(proposta[3])
        status=proposta[4]
        idProposta=proposta[5]

        propostas.append( Proposta(usuarioAlvo=usuarioRequisitado,usuarioRequisitante=usuarioRequisitante,
        idProposta=idProposta,movelProposto=movelProposto,movelRequerido=movelRequisitado,status=status))
    return propostas

def aceitaProposta(idProposta:int,cpfUsuarioAlvo:int)->int:
    try:

        proposta = buscaProposta(idProposta=idProposta)
        
        updateMovelCpf(proposta.movelRequerido.id,proposta.usuarioRequisitante.cpf)
        updateMovelCpf(proposta.movelProposto.id,proposta.usuarioAlvo.cpf)
        deletarMovel(idMovel=proposta.movelProposto.id,cpf=proposta.usuarioRequisitante.cpf)
        deletarMovel(idMovel=proposta.movelRequerido.id,cpf=proposta.usuarioAlvo.cpf)
        vsql="UPDATE Proposta SET status=1 WHERE (idProposta = '"+str(idProposta)+"'AND usuarioAlvo = '"+str(cpfUsuarioAlvo)+"');"
        ExecutaSQL(vcon,vsql)
        return StatusResposta.sucesso.value
    except:
        return StatusResposta.falha.value

def recusaProposta(idProposta:int,cpfUsuarioAlvo:int):
    try:
        vsql="UPDATE Proposta SET status=-1 WHERE (idProposta = '"+str(idProposta)+"'AND usuarioAlvo = '"+str(cpfUsuarioAlvo)+"');"
        ExecutaSQL(vcon,vsql)
        return StatusResposta.sucesso.value
    except:
        return StatusResposta.falha.value

def buscaProposta(idProposta:int)->Proposta:
    try:
        vsql="SELECT * FROM Proposta WHERE idProposta == '"+str(idProposta)+"'; "
        result = ExecutaSQL(vcon,vsql).fetchone()
        usuarioAlvo=buscarUsuarioBancoCpf(result[1])
        usuarioRequisitante=buscarUsuarioBancoCpf(result[0])
        movelProposto = buscaMovel(result[2])
        movelRequerido = buscaMovel(result[3])
        idProposta=result[5]
        status = result[4]
        proposta= Proposta(idProposta,usuarioRequisitante,usuarioAlvo,movelProposto,movelRequerido,status)
        return proposta
    except Exception as e:
        print('Exception occurred while code execution: ' + str(e))

def updateMovelCpf(idMovel:int,cpf:int):
    try:
        vsql="UPDATE Movel SET usuario_cpf == '"+str(cpf)+"' WHERE idMovel= '"+str(idMovel)+"';"
        ExecutaSQL(vcon,vsql)
        
    except Exception as e:
        print(str(e))


    






