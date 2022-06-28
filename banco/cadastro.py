import sqlite3
import sys
import os

from sqlite3 import Error
sys.path.append(os.path.abspath('./'))
from models.usuario import Usuario
from models.proposta import StatusProposta


#Conectando ou criando o banco 
def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect('CadastroUser.bd')
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

        nome=user.nome
        senha=user.senha
        cpf=str(user.cpf)
        vsql="INSERT INTO tb_Cadastro(T_NOME,T_SENHA,T_CPF)VALUES('"+nome+"','"+senha+"','"+cpf+"')"
        ExecutaSQL(vcon,vsql)

        #StatusProposta.aceito.value #Cadastrado com sucesso
    
        #StatusProposta.recusado.value #Erro no cadastro


def buscarBanco(cpf:str):
    vsql="SELECT * FROM tb_Cadastro WHERE T_CPF == '"+cpf+"'; "
    print(ExecutaSQL(vcon,vsql).fetchone())


def atualizaBanco(user:Usuario):
    nome=user.nome
    senha=user.senha
    cpf=str(user.cpf)
    vsql="UPDATE tb_Cadastro SET T_CPF == '"+cpf+"', T_NOME == '"+nome+"', T_SENHA == '"+senha+"' WHERE N_IDCADASTRO=3"
    ExecutaSQL(vcon,vsql)


'''def listandoBanco():
    
    vsql="SELECT * FROM CadastroUsuario"
    data=ExecutaSQL(vcon,vsql)

    for row in data:
        print(row)'''

#----------TESTE PARA O BANCO----------#
if __name__ == "__main__":
    usuario = Usuario("nome", "senha", 123,
                 "moveis", [], []) 

    inserirBanco(usuario)
    #buscarBanco(str(usuario.cpf))
    #atualizaBanco(usuario)
    #listandoBanco()

    print("deu bom")


'''
#------------CRIANDO A TABELA DE CADASTRO----------#

vsql = """CREATE TABLE tb_Cadastro(
    N_IDCADASTRO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOME VARCHAR(30),
    T_SENHA VARCHAR(40),
    T_CPF VARCHAR(40)
);"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)'''



'''
nome=input("Inisra o Nome: ")
senha=input("Inisra o Senha: ")
endereco=input("Inisra o Endereco: ")
telefone=input("Inisra o Telefone: ")
email=input("Inisra o Email: ")
cpf=input("Inisra o CPF: ")
'''