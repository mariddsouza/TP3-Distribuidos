from colorama import Fore 
from colorama import Style
class Cores:
    def __init__(self) -> None:
        self.corIniFimTela = Fore.MAGENTA
        self.corOpcoes = Fore.BLUE
        self.corErro= Fore.RED
        self.corSucesso = Fore.GREEN
        self.corEntrada = Fore.LIGHTYELLOW_EX 
    def criarTextoTela(self,string:str)-> str:
        return self.corIniFimTela+string+Fore.RESET
    def criarTextoOpcoes(self,string:str)-> str:
        return self.corOpcoes+string+Fore.RESET
    def criarTextoErro(self,string:str)-> str:
        return self.corErro+string+Fore.RESET
    def criarTextoSucesso(self,string:str)-> str:
        return self.corSucesso+string+Fore.RESET
    def criarTextoEntrada(self,string:str)-> str:
        return (self.corEntrada+string+Fore.RESET)
