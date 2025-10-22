import random

class Cliente:
    def __init__(self, id, name, tel, mail):
        self.id = id
        self.name = name
        self.tel = tel
        self.mail = mail
    
    def __str__(self):
        return(f"{self.id} - {self.name} - {self.tel} - {self.mail}")
    
class SistemaClientes():
    Tclientes = []
        
    def cadastrarCliente(self):
        name = input("Qual o nome desse Clientes?")
        tel = input("Qual o telefone desse Clientes?")
        mail = input("Qual o E-mail desse Clientes?")
        cliente = Cliente(len(self.Tclientes), name, tel, mail)
        self.Tclientes.append(cliente)
        
    def listarCliente(self):
        for cliente in self.Tclientes:
            print(cliente)
        
    def removerCliente(self):
        print("Para remover um usuário da lista, digite seu ID:")
        id = int(input("> "))
        self.Tclientes.pop(int(id))
        


sistema = SistemaClientes()

#Cadastrando 2 Clientes
sistema.cadastrarCliente()
sistema.cadastrarCliente()
sistema.listarCliente()
sistema.removerCliente()
sistema.listarCliente()
