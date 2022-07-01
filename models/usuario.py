class Usuario:
    def __init__(self, nome: str, senha: str,cpf: int,
                 moveis=[], propostasRecebidas=[], propostasFeitas =[]) -> None:
        self.nome: str = nome
        self.senha: str = senha
        self.cpf: int = cpf
        self.moveis: list = moveis
        self.propostasFeitas: list = propostasFeitas
        self.propostasRecebidas: list = propostasRecebidas

