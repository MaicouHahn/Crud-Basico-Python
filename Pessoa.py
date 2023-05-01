class Pessoa:

    def __init__(self,nome,cpf) :
        self.nome=nome
        self.cpf=cpf

    def mostrar_dados(self):#seria a mesma coisa que em java passar mostrar_dados(Pessoa pessoa)
        print("Nome: ",self.nome)
        print("Cpf> ",self.cpf)

    @staticmethod
    def validar_cpf(cpf)->bool:#tipagem booleana para o metodo
        if len(cpf)==11:
            return True
        else:
            return False
    