#Aqui criaremos os relatórios
import estoque, servicos

class Relatorio:
    def __init__(self, id, nome, tipo, gerado):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.gerado = gerado
    
class sistemaRelatorios():
    def relatorioDePeças(self):
        for peca in estoque.SistemaEstoque.t_Estoque:
            if peca.qtd < 5:
                print("-=" * 30)
                print("RELATÓRIO DE PEÇAS")
                print("QUANTIDADE BAIXA")
                print(peca)
        print(" ")
    
    def relatorioDeServicos(self):
        for servico in servicos.SistemaServicos.l_servicos:
            if servico.status_input == 3:
                print("-=" * 30)
                print("RELATÓRIO DE SERVIÇO")
                print(servico)
        print(" ")
    
            
