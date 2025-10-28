#Cadastro de serviços
class Servicos:
    def __init__(self, id, name, desc, preco, status, status_input):
        self.id = id
        self.name = name
        self.desc = desc
        self.preco = preco
        self.status = status
        self.status_input = status_input
    
    def __str__(self):
        return(f"{self.id} | Serviço: {self.name} | Preço {self.preco} \nStatus: {self.status} | Descrição: {self.desc}\n" + "-=" * 20)
    
class SistemaServicos():
    l_servicos = []
     
    def cadastroServico(self):
        name = input("Digite o nome do serviço: ")
        preco = input("Digite o preço do serviço: R$")
        desc = input("Digite uma breve descrição para o serviço: ")

        status_input = int(input("Escolha o status do serviço:\n1 - Na bancada\n2 - Aguardando peça\n3 - Pronto para retirada\n4 - Entregue\n> "))

        
        match int(status_input):
            case 1:
                status = "Na bancada"
            case 2:
                status = "Aguardando peça"
            case 3:
                status = "Pronto para retirada"
            case 4:    
                status = "Entregue"
        
        servico = Servicos(len(self.l_servicos), name, preco, desc, status, status_input)
        self.l_servicos.append(servico)
        #print("Serviço cadastrado com sucesso!")
        
        
    def listarServicos(self):
        print("Agora irei listar os serviços!")
        for servico in self.l_servicos:
            print(servico)
    
    def removerServico(self):
        remover = input("Qual serviço você quer remover? DIGITE O ID\n> ")
        self.l_servicos.pop(int(remover))
        
    def atualizarStatus(self):
        pass