import mysql.connector

class ConnectionDAO:

    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.conn=mysql.connector.connect(host=host, user=user, password=password, database=database)
        
        self.conexao=self.conn.cursor()

    def close_con(self):
        self.conexao.close()
        self.conn.close()


    def query_BD(self,query):
        self.conexao.execute(query)
        res=self.conexao.fetchall()
        return res

    def insert_BD(self,valores):#esse valores é uma tupla no caso é ("nome","cpf"), a syntaxe nao muda pois ela varia para casos e bancos apenas
        self.conexao.execute("insert into pessoa(nomepessoa,cpfpessoa) values(%s,%s)",valores)
        self.conn.commit()

    def alter_BD(self,dados):
        self.conexao.execute("update pessoa set nomepessoa=%s,cpfpessoa=%s where idpessoa=%s",dados)
        self.conn.commit()

    def delete_BD(self,id):
        self.conexao.execute("Delete from pessoa where idpessoa = %s",id)
        self.conn.commit()