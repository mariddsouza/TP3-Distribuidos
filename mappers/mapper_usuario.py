from models.usuario import Usuario

class MapperUsuario:
    def __init__(self) -> None:
        pass
    def usuarioToJson(usuario:Usuario) -> dict:
        dicionario = {}
        dicionario['nome']=usuario.nome
        dicionario['senha'] = usuario.senha
        dicionario['cpf'] = usuario.cpf
        return dicionario 
    
    def jsonToUsuario(dicionario:dict) -> Usuario:
        nome:str=dicionario['nome']
        senha:str=dicionario['senha'] 
        cpf:int=dicionario['cpf'] 
       
        return Usuario(nome=nome,senha=senha,cpf=cpf)
