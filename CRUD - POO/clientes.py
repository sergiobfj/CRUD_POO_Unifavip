# Cadastro de clientes finalizada


class Cliente: #Classe do Cliente
    def __init__(self, name, tel, mail): #Atributos do cliente
        self.name = name
        self.tel = tel
        self.mail = mail
    
    def __str__(self):
        return(f"{self.name} | Telefone: {self.tel} - E-Mail:{self.mail}") #Função que retorna a formatação do texto no terminal
    
class SistemaClientes(): #Classe do Sistema de Cadastro de Clientes
    Tclientes = [] #Lista de clientes
        
    def cadastrarCliente(self): #Método de cadastro de clientes
        name = input("Nome Completo: ").upper()

        while True: #Tratamento de erro
            tel = input("Telefone (APENAS NÚMEROS): ")
            if len(tel) != 11:
                print("O número não tem a quantidade correta de digitos. Corrija: ")
                continue      
            else:
                break

        while True: #tratamento de erro
            mail = input("E-mail: ")
            if '@' not in mail:
                print("Digite o E-mail corretamente.")
                continue
            else:
                break

        cliente = Cliente(name, tel, mail) #Criando as instâncias
        self.Tclientes.append(cliente) #Adcionando os clientes na lista
        
    def listarCliente(self): #Método de listar clientes
        for cliente in self.Tclientes:
            print("-="*30)
            print(cliente)

    def removerCliente(self):
        while True:
            print("Para remover um usuário da lista, digite seu Nome Completo (ou 'SAIR' para sair):")
            nome = input("> ").strip().upper()

            if nome == 'SAIR': 
                print("Operação cancelada.")
                return

            for cliente in self.Tclientes: #Tratamento de erro:
                if cliente.name == nome:
                    opc = input(f"Tem certeza que quer excluir o cliente {cliente.name}? [S/N] ").strip().upper()
                    if opc == 'S':
                        self.Tclientes.remove(cliente)
                        print("Cliente removido com sucesso.")
                    else:
                        print("Remoção cancelada.")
                    return  # Sai do método após tratar o cliente
            print("Esse cliente não existe. Tente novamente.\n")

        

#Testes -- Apagar quando o MAIN estiver pronto
sistema = SistemaClientes()

#Cadastrando 2 Clientes
sistema.cadastrarCliente()
sistema.listarCliente()
sistema.removerCliente()
sistema.listarCliente()
