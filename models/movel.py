
class Movel:
    def __init__(self,id:int, nome:str,fotos:list, tempoUso:int, descricao:str) -> None:
        self.id : int = id
        self.nome : str = nome
        self.fotos: list = fotos
        self.tempoUso : int = tempoUso
        self.descricao : str = descricao