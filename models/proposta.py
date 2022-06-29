from models.movel import Movel
from models.usuario import Usuario
from enum import Enum


class StatusProposta(Enum):
    emEspera=0,
    aceito=1,
    recusado=-1,

class Proposta:
    def __init__(self,usuarioRequisitante: Usuario, usuarioAlvo: Usuario, moveisPropostos:Movel,moveisRequeridos:Movel, status:StatusProposta) -> None:
        self.idProposta = 0
        self.usuarioRequisitante: Usuario = usuarioRequisitante
        self.usuarioAlvo: Usuario = usuarioAlvo
        self.moveisPropostos:Movel = moveisPropostos
        self.moveisRequeridos: Movel = moveisRequeridos
        self.status : StatusProposta = status

