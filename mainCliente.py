from cliente.cadastro import Cadastro
from cliente.cores import Cores
# from cliente.cliente import Cliente

from cliente.login import Login
from models.status_resposta import StatusResposta


# cliente:Cliente = Cliente()
op=1
cores=Cores()
while op!=0:
    op=Login.menu()
    if op == 1:
        pass
    elif op == 2:
        status = Cadastro.menu()
        if status == StatusResposta.sucesso.value:
            print(cores.criarTextoSucesso("Cadastro realizado com sucesso!"))
        else:
            print(cores.criarTextoErro("Cadastro não pôde ser realizado com sucesso!"))
        print()
        