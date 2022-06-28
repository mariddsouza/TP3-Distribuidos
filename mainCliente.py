from cliente.cadastro import Cadastro
from cliente.cores import Cores
from cliente.home import Home
# from cliente.cliente import Cliente

from cliente.login import Login
from models.status_resposta import StatusResposta


# cliente:Cliente = Cliente()
opLogin=1
cores=Cores()
while opLogin!=0:
    opLogin=Login.menu()
    if opLogin == 1:
        usuario = Login.login()
        if usuario is not None:
            print(cores.criarTextoSucesso("\nLogin realizado com sucesso!"))
            print(cores.criarTextoSucesso("Seja bem-vindo {}.\n".format(usuario.nome)))
            opHome = Home.menu()
            while opHome != 0:
                if opHome == 1:
                    Home.mostrarMoveis(usuario.moveis)
                elif opHome == 2:
                    Home.cadastrarMovel()
                elif opHome == 3:
                    pass
                elif opHome == 4:
                    pass
                elif opHome == 5:
                    pass
                elif opHome == 6:
                    pass
        else:
            print(cores.criarTextoErro("\nLogin não pôde ser realizado com sucesso!\n"))
    
    elif opLogin == 2:
        status = Cadastro.menu()
        if status == StatusResposta.sucesso.value:
            print(cores.criarTextoSucesso("Cadastro realizado com sucesso!"))
        else:
            print(cores.criarTextoErro("Cadastro não pôde ser realizado com sucesso!"))
        print()
print(cores.criarTextoTela("---------- FIM TELA DE LOGIN ----------"))