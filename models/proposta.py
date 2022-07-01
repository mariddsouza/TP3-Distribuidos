from models.movel import Movel
from models.usuario import Usuario
from enum import Enum


class StatusProposta(Enum):
    EmEspera=0
    Aceito=1
    Recusado=-1

class Proposta:
    def __init__(self,idProposta:int,usuarioRequisitante: Usuario, 
        usuarioAlvo: Usuario, movelProposto:Movel,movelRequerido:Movel, status:int) -> None:
        self.idProposta:int = idProposta
        self.usuarioRequisitante: Usuario = usuarioRequisitante
        self.usuarioAlvo: Usuario = usuarioAlvo
        self.movelProposto:Movel = movelProposto
        self.movelRequerido: Movel = movelRequerido
        self.status : int = status

