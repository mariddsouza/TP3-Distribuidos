import sqlite3
import sys
import os

from sqlite3 import Error
from typing import List
from models.status_resposta import StatusResposta
sys.path.append(os.path.abspath('./'))
from models.usuario import Usuario
from models.movel import Movel
from models.proposta import Proposta

#criando o banco 
def criarBanco():
    cursor = sqlite3.connect("UserCadastro.bd").cursor()
    sql_file = open("banco/criarBanco.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
    cursor.close()


#Acessando o banco 
def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect('UserCadastro.bd')
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
        # print("Cadastro inserido com sucesso ")
        vsql="SELECT * FROM Usuario WHERE cpf == {}".format(cpf)
        result = ExecutaSQL(vcon,vsql).fetchone()
        if(result==None):
            vsql="INSERT INTO Usuario(nome,senha,cpf)VALUES('"+nome+"','"+senha+"','"+cpf+"')"
            ExecutaSQL(vcon,vsql)
            # vsql="SELECT * FROM Usuario ORDER BY rowid DESC LIMIT 1;"
            # ExecutaSQL(vcon,vsql).fetchone()
            return StatusResposta.sucesso.value
        else:
            return StatusResposta.falha.value 
    except :
        # print("entrou no errado")
        return StatusResposta.falha.value #Erro no cadastro
       
def inserirMovel(cpf:str, movel:Movel):
    try:
        nome=movel.nome
        tempoUso=movel.tempoUso
        descricao=movel.descricao
        vsql="INSERT INTO Movel(nome,tempoUso,descricao,Usuario_cpf) VALUES('"+nome+"','"+str(tempoUso)+"','"+descricao+"','"+str(cpf)+"');"
        ExecutaSQL(vcon,vsql)
        #Fazer tratamento de erro 
        #retorna o id do movel
        # vsql="select last_insert_rowid()"
        # ExecutaSQL(vcon,vsql).fetchone()[0]
        return  StatusResposta.sucesso.value
    except Error:
        return StatusResposta.falha.value



def deletarMovel(idMovel:int):
    try:
        vsql="DELETE FROM Movel WHERE idMovel == '"+str(idMovel)+"';"
        ExecutaSQL(vcon,vsql)
        return StatusResposta.sucesso.value
    except:
        return StatusResposta.falha.value

def buscarUsuarioBanco(cpf:str,senha:str)->Usuario:
    vsql="SELECT * FROM Usuario WHERE cpf =='"+cpf+"' AND senha == '"+senha+"';"
    result=ExecutaSQL(vcon,vsql).fetchone()
    print(result)
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


def listarUsuarios():
    vsql="SELECT * FROM Usuario ; "
    return ExecutaSQL(vcon,vsql).fetchall()
 
def buscarMoveis(cpf)-> List[Movel]:
    moveis = []
    vsql="SELECT * FROM Movel WHERE Usuario_cpf == "+str(cpf)+";"
    result = ExecutaSQL(vcon,vsql).fetchall()
    for movel in result:
        moveis.append( Movel(id=movel[0],nome=movel[1],descricao=movel[3],tempoUso=movel[2]))
    return moveis


def criarProposta(idMovelRequirido: int, idMovelProposto: int, cpfUsuarioRequisitante:str, cpfUsuarioAlvo:str):
    vsql="INSERT INTO Proposta(usuarioRequisitante, usuarioAlvo, moveisPropostos, moveisRequiridos, status)VALUES('"+str(cpfUsuarioRequisitante)+"','"+str(cpfUsuarioAlvo)+"','"+str(idMovelProposto)+"','"+str(idMovelRequirido)+"',0)"
    ExecutaSQL(vcon,vsql)

def buscaMovel(idMovel:int):
    vsql="SELECT * FROM Movel WHERE idMovel == '"+str(idMovel)+"'; "
    querry= ExecutaSQL(vcon,vsql).fetchone()
    return Movel(querry[1],querry[2],querry[3],querry[0])

def buscaPropostaRealizada(cpf:int):
    vsql="SELECT * FROM Proposta WHERE usuarioRequisitante == '"+str(cpf)+"'; "
    return ExecutaSQL(vcon,vsql).fetchall()

def buscaPropostaRecebida(cpf:int):
    vsql="SELECT * FROM Proposta WHERE usuarioAlvo == '"+str(cpf)+"'; "
    return ExecutaSQL(vcon,vsql).fetchall()

def aceitaProposta(idMovelRequirido: int, idMovelProposto: int, cpfUsuarioRequisitante:str, cpfUsuarioAlvo:str):
    vsql="UPDATE Proposta SET status=1 WHERE (usuarioRequisitante = '"+str(cpfUsuarioRequisitante)+"'AND usuarioAlvo = '"+str(cpfUsuarioAlvo)+"'AND moveisPropostos = '"+str(idMovelProposto)+"'AND moveisRequiridos = '"+str(idMovelRequirido)+"');"
    ExecutaSQL(vcon,vsql)

def recusaProposta(idMovelRequirido: int, idMovelProposto: int, cpfUsuarioRequisitante:str, cpfUsuarioAlvo:str):
    vsql="UPDATE Proposta SET status=-1 WHERE (usuarioRequisitante = '"+str(cpfUsuarioRequisitante)+"'AND usuarioAlvo = '"+str(cpfUsuarioAlvo)+"'AND moveisPropostos = '"+str(idMovelProposto)+"'AND moveisRequiridos = '"+str(idMovelRequirido)+"');"
    ExecutaSQL(vcon,vsql)


#----------TESTE PARA O BANCO----------#
if __name__ == "__main__":
    usuario1 = Usuario("Mariana", "senha", 380033,
                 "moveis", [], []) 
    usuario2 = Usuario("jao", "senha", 3506,
    "moveis", [], []) 

    movel1 = Movel("cadeira", 10, "meu movel",2)
    movel2 = Movel("mesa", 45, "meu movel",3)

    proposta = Proposta(usuario1, usuario2, movel1, movel2, 0)

    #print(inserirMovel(str(usuario1.cpf),movel1))
    #deletarMovel(1)
    #print(listarUsuarios())
    #print(inserirUsuario(usuario1))
    #criarProposta(proposta.moveisRequeridos.id,proposta.moveisPropostos.id,proposta.usuarioRequisitante.cpf,proposta.usuarioAlvo.cpf)
    #print((buscarBanco(str(usuario.cpf))[0]))
    #atualizaBanco(usuario)
    #listandoBanco()
    #print(buscaMovel(4))
    #print(buscaPropostaRealizada(380033))
    #print(buscaPropostaRecebida(3506))
    #aceitaProposta(0 , 0, '380033', '3506')
    #recusaProposta(0 , 0, '380033', '3506')

    #criarBanco()

    print("deu bom")





