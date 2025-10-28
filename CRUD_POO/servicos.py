#Cadastro de serviços
class Servicos:
    def __init__(self, id, name, desc, preco, status):
        self.id = id
        self.name = name
        self.desc = desc
        self.preco = preco
        self.status = status
    
    def __str__(self):
        return(f"{self.id} | Serviço: {self.name} | Preço {self.preco} \nStatus: {self.status} | Descrição: {self.desc}\n" + "-=" * 20)
    
class SistemaServicos():
    l_servicos = []
     
    def cadastroServico(self):
        name = input("Digite o nome do serviço: ")
        preco = input("Digite o preço do serviço: R$")
        desc = input("Digite uma breve descrição para o serviço: ")
        status_input = int(input("Escolha o status do serviço:\n1 - Na bancada\n2 - Aguardando peça\n3 - Pronto para retirada\n4 - Entregue\n> "))   
        
        match status_input:
            case 1:
                status = "Na bancada"
            case 2:
                status = "Aguardando peça"
            case 3:
                status = "Pronto para retirada"
            case 4:    
                status = "Entregue"
        
        servico = Servicos(len(self.l_servicos), name, preco, desc, status)
        self.l_servicos.append(servico)
        print("Serviço cadastrado com sucesso!")
        
    def listarServicos(self):
        print("Agora irei listar os serviços!")
        for servico in self.l_servicos:
            #print(f"{servico} | Serviço: {servico} | Preço {servico} \nStatus: {servico} | Descrição: {servico}\n" + "-=" * 20)
            print(servico)
            
#print(f"{10} | Serviço: {"TESTE"} | Preço {1000} \nStatus: {"OFF"} | Descrição: {"TESTANDO"}\n" + "-=" * 20)

servicos = SistemaServicos()

servicos.cadastroServico()
servicos.cadastroServico()
servicos.listarServicos()