from Connection import ConnectionDAO
from Pessoa import Pessoa
p1=Pessoa("Rafael","1234")

c1= ConnectionDAO("localhost","root","","teste")


#valores=("asasdsad","12343423")
#c1.insert_BD(valores)

resultado = c1.query_BD("SELECT * FROM pessoa")
for res in resultado:
    print(res)
print("======================================")

li=[2]
c1.delete_BD(li)

dados=(p1.nome,p1.cpf,10)

c1.alter_BD(dados)
resultado = c1.query_BD("SELECT * FROM pessoa")
for res in resultado:
    print(res)


c1.close_con()
