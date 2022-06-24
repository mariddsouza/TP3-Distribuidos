from enum import Enum


class TipoOperacao(Enum):
    criarUsuario = 0
    buscarUsuario = 1
    alterarUsuario = 2

    proporTroca = 3
    aceitarTroca = 4
    recusarTroca = 5

    buscarMovel = 6
