from models.usuario import Usuario
from enum import Enum


class StatusProposta(Enum):
    emEspera=0,
    aceito=1,
    recusado=-1,

class Proposta:
    def __init__(self,usuarioRequisitante: Usuario, moveisPropostos:list,moveisRequeridos:list, status:StatusProposta) -> None:
        self.usuarioRequisitante: Usuario = usuarioRequisitante
        self.moveisPropostos:list = moveisPropostos
        self.moveisRequeridos: list = moveisRequeridos
        self.status : StatusProposta = status

