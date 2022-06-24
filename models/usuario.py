from models.movel import Movel


class Endereco:
    def __init__(self, rua: str, numero: int, bairro: str, cep: str, ) -> None:
        self.rua: str = rua
        self.numero: int = numero
        self.bairro: str = bairro
        self.cep: str = cep


class Usuario:
    def __init__(self, nome: str, senha: str, endereco: Endereco,
                 telefone: str, email: str, cpf: int,
                 moveis: list, propostasRecebidas: list, propostasFeitas: list) -> None:
        self.nome: str = nome
        self.senha: str = senha
        self.endereco: Endereco = endereco
        self.telefone: str = telefone
        self.email: str = email
        self.cpf: int = cpf
        self.moveis: list = moveis
        self.propostasFeitas: list = propostasFeitas
        self.propostasRecebidas: list = propostasRecebidas
