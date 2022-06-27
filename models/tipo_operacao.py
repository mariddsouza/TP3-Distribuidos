from enum import Enum


class TipoOperacao(Enum):
    criarUsuario = 0
    buscarUsuario = 1
    alterarUsuario = 2
    buscarTodosUsuarios = 3

    proporTroca = 4
    aceitarTroca = 5
    recusarTroca = 6