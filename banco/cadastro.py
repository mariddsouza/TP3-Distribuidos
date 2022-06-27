import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect('CadastroUsuario.bd')
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()


nome=input("Inisra o Nome: ")
senha=input("Inisra o Senha: ")
endereco=input("Inisra o Endereco: ")
telefone=input("Inisra o Telefone: ")
email=input("Inisra o Email: ")
cpf=input("Inisra o CPF: ")



vsql="INSERT INTO tb_CadastroUser(T_NOME,T_SENHA,T_ENDERECO,T_TELEFONE,T_EMAIL,T_CPF)VALUES('"+nome+"','"+senha+"','"+endereco+"','"+telefone+"','"+email+"','"+cpf+"')"

def inserir(conexao,sql):
    try:
        print("aqui")
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("entrooouuuu")
    except Error as ex:
        print(ex)

inserir(vcon,vsql)

'''
####CRIANDO A TABELA DE CADASTRO########

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

