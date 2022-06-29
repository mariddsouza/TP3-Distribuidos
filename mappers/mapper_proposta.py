from mappers.mapper_movel import MapperMovel
from mappers.mapper_usuario import MapperUsuario
from models.proposta import Proposta
from models.usuario import Usuario


class MapperProposta:
    def __init__(self) -> None:
        pass
    def propostaToJson(proposta:Proposta) -> dict:
        dicionario={}
        movelProposto = proposta.movelProposto
        movelRequerido = proposta.movelRequerido
        usuarioRequisitante = proposta.usuarioRequisitante
        usuarioRequisitado = proposta.usuarioRequisitado 
        dicionario ['status']= proposta.status.value
        dicionario['movelProposto']= MapperMovel.movelToJson(movel=movelProposto)
        dicionario['movelRequerido']= MapperMovel.movelToJson(movel=movelRequerido)
        dicionario['usuarioRequisitante'] = MapperUsuario.usuarioToJson(usuario=usuarioRequisitante)
        dicionario['usuarioRequisitado'] = MapperUsuario.usuarioToJson(usuario=usuarioRequisitado)
        return dicionario 
    
    def jsonToProposta(dicionario:dict) -> Proposta:
        status=dicionario ['status']
        movelProposto=MapperMovel.jsonToMovel(dicionario['movelProposto'])
        movelRequerido=MapperMovel.jsonToMovel(dicionario['movelRequerido'])
        usuarioRequisitante=MapperUsuario.jsonToUsuario(dicionario['usuarioRequisitante'])
        usuarioRequisitado=MapperUsuario.jsonToUsuario(dicionario['usuarioRequisitado']) 
       
        return Proposta(status=status,movelProposto=movelProposto,movelRequerido=movelRequerido
        ,usuarioRequisitado=usuarioRequisitado,usuarioRequisitante=usuarioRequisitante)