from models.movel import Movel
from models.usuario import Usuario
from enum import Enum


class StatusProposta(Enum):
    emEspera=0,
    aceito=1,
    recusado=-1,

class Proposta:
    def __init__(self,usuarioRequisitante: Usuario, movelProposto:Movel,id:int,
    movelRequerido:Movel, status:StatusProposta) -> None:
        self.usuarioRequisitante: Usuario = usuarioRequisitante
        self.movelProposto:Movel= movelProposto
        self.id:int=id
        self.movelRequerido: Movel= movelRequerido  
        self.status : StatusProposta = status

