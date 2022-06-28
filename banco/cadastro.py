import sqlite3
import sys
import os

from enum import Enum
from sqlite3 import Error
from models.proposta import StatusProposta
sys.path.append(os.path.abspath('./'))
from models.usuario import Usuario

#Conectando ou criando o banco 
def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect('CadastroUsuario.bd')
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


def inserirBanco(user:Usuario):
    try:
        nome=user.nome
        senha=user.senha
        endereco=user.endereco
        telefone=user.telefone
        email=user.email
        cpf=str(user.cpf)
        vsql="INSERT INTO tb_CadastroUser(T_NOME,T_SENHA,T_ENDERECO,T_TELEFONE,T_EMAIL,T_CPF)VALUES('"+nome+"','"+senha+"','"+endereco+"','"+telefone+"','"+email+"','"+cpf+"')"
        ExecutaSQL(vcon,vsql)

        StatusProposta.aceito #Cadastrado com sucesso
    except Error:
        StatusProposta.recusado #Erro no cadastro


def buscarBanco(cpf:str):
    vsql="SELECT * FROM tb_CadastroUser WHERE T_CPF == '"+cpf+"'; "
    print(ExecutaSQL(vcon,vsql).fetchone())


def atualizaBanco(user:Usuario):
    nome=user.nome
    senha=user.senha
    endereco=user.endereco
    telefone=user.telefone
    email=user.email
    cpf=str(user.cpf)
    vsql="UPDATE tb_CadastroUser SET T_CPF == '"+cpf+"', T_NOME == '"+nome+"', T_ENDERECO == '"+endereco+"', T_TELEFONE == '"+telefone+"', T_EMAIL == '"+email+"', T_SENHA == '"+senha+"' WHERE N_IDCADASTRO=3"
    ExecutaSQL(vcon,vsql)


'''def listandoBanco():
    
    vsql="SELECT * FROM CadastroUsuario"
    data=ExecutaSQL(vcon,vsql)

    for row in data:
        print(row)'''




'''
#----------TESTE PARA O BANCO----------#
if __name__ == "__main__":
    usuario = Usuario("Mariana teste 7", "123", "rua rua bairro bairro",
                 "31 9 82400000", "maria@gamail.com", 123,
                 "moveis", [], []) 

    inserirBanco(usuario)
    #buscarBanco(str(usuario.cpf))
    #atualizaBanco(usuario)
    #listandoBanco()

    print("deu bom")'''



'''
#------------CRIANDO A TABELA DE CADASTRO----------#

vsql = """CREATE TABLE tb_CadastroUser(
    N_IDCADASTRO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOME VARCHAR(30),
    T_SENHA VARCHAR(40),
    T_ENDERECO VARCHAR(50),
    T_TELEFONE VARCHAR(14),
    T_EMAIL VARCHAR(30),
    T_CPF VARCHAR(40)
);"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("CRIOOUUU")
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)
'''


'''
nome=input("Inisra o Nome: ")
senha=input("Inisra o Senha: ")
endereco=input("Inisra o Endereco: ")
telefone=input("Inisra o Telefone: ")
email=input("Inisra o Email: ")
cpf=input("Inisra o CPF: ")
'''