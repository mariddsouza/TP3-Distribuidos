from models.usuario import Endereco, Usuario

class MapperUsuario:
    def __init__(self) -> None:
        pass
    def usuarioToJson(usuario:Usuario) -> dict:
        dicionario = MapperUsuario.enderecoToJson(usuario.endereco)
        dicionario['nome']=usuario.nome
        dicionario['senha'] = usuario.senha
        dicionario['cpf'] = usuario.cpf
        dicionario['telefone'] = usuario.telefone
        dicionario['email'] = usuario.email
        return dicionario 

    def enderecoToJson(endereco:Endereco)->dict:
        dicionario = {}
        dicionario['rua']=endereco.rua
        dicionario['cep']=endereco.cep
        dicionario['bairro']=endereco.bairro
        dicionario['numero']=endereco.numero
        return dicionario
    
    def jsonToUsuario(dicionario:dict) -> Usuario:
        nome:str=dicionario['nome']
        senha:str=dicionario['senha'] 
        cpf:int=dicionario['cpf'] 
        telefone:str=dicionario['telefone'] 
        email:str=dicionario['email']
        endereco:Endereco = MapperUsuario.jsonToEndereco(dicionario)
        return Usuario(nome=nome,senha=senha,cpf=cpf,telefone=telefone,email=email,endereco=endereco)


    def jsonToEndereco(dicionario:dict) -> Endereco:
        rua: str = dicionario['rua']
        cep : str= dicionario['cep']
        bairro : str =dicionario['bairro']
        numero :int=dicionario['numero']
        return Endereco(rua=rua,cep=cep,bairro=bairro,numero=numero)
