from banco.cadastro import criarProposta
from cliente.cliente import Cliente
from cliente.home import Home
from cliente.login import Login
# print(buscarMoveis(33333)[0].nome)
# criarProposta(2,4,2505,1234)
# criarProposta(2,4,2505,1234)
# criarProposta(2,4,1234,2505)
# criarProposta(2,4,1234,2505)
cliente:Cliente = Cliente()
home:Home = Home(cliente=cliente)
login:Login = Login(cliente=cliente)
login.menu()