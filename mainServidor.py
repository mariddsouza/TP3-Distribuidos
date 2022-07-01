import threading
from mappers.mapper_movel import MapperMovel
from mappers.mapper_proposta import MapperProposta
from mappers.mapper_usuario import MapperUsuario

from models.tipo_operacao import TipoOperacao
from models.usuario import Usuario
from servidor.servidor import Servidor

servidor: Servidor = Servidor()

while True:
    con, cliente = servidor.tcp.accept()
    print ('Conectado por ', cliente)
    threading.Thread(target=servidor.inicializar, args=(con,)).start()
    print ('Finalizando conexão do cliente', cliente)


    


