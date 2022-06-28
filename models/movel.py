
class Movel:
    def __init__(self,id:int, nome:str, tempoUso:int, descricao:str) -> None:
        self.id : int = id
        self.nome : str = nome
        self.tempoUso : int = tempoUso
        self.descricao : str = descricao