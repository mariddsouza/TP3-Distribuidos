from cliente.cliente import Cliente
from models.usuario import Usuario,Endereco

cliente:Cliente = Cliente()

# endereco:Endereco= Endereco(rua="Rua A",bairro="Vila Operária",cep="39100-000",numero=35)
# usuario:Usuario=Usuario(nome="Fabio",cpf=10656980621,endereco=endereco,email="email@email.com",
# moveis=[],senha="senha",telefone="(38)988337225",propostasFeitas=[],propostasRecebidas=[])
# cliente.criarUsuario(usuario=usuario)
# cliente.alterarUsuario(usuario=usuario)
lista=cliente.buscarTodosUsuarios()
print(lista[0].nome)

