
class Movel:
    def __init__(self, nome:str, tempoUso:int, descricao:str,id : int = 0)  -> None:
        self.id : int =  id
        self.nome : str = nome
        self.tempoUso : int = tempoUso
        self.descricao : str = descricao