import re
from models.movel import Movel


class MapperMovel:
    def __init__(self) -> None:
        pass

    def movelToJson(movel:Movel):
        dicionario: dict = {}
        dicionario['id']=movel.id
        dicionario['descricao']=movel.descricao
        dicionario['nome']=movel.nome
        dicionario['tempoUso']=movel.tempoUso
        return dicionario

    def jsonToMovel(dicionario:dict):
        id=dicionario['id']
        descricao=dicionario['descricao']
        nome=dicionario['nome']
        tempouso=dicionario['tempoUso']
        return Movel(id=id,tempoUso=tempouso,descricao=descricao,nome=nome)