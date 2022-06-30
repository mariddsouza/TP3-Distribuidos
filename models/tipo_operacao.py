from enum import Enum


class TipoOperacao(Enum):
    criarUsuario = 0
    buscarUsuario = 1
    alterarUsuario = 2
    buscarTodosUsuarios = 3

    proporTroca = 4
    aceitarTroca = 5
    recusarTroca = 6
    
    criarMovel = 7
    excluirMovel = 8
    buscarMoveis = 9

    buscarPropostasRealizadas=10
    buscarPropostasRecebidas=11
