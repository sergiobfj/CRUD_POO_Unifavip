import random

class Estoque:
    def __init__(self, id, name, preco, qtd):
        self.id = id
        self.name = name
        self.preco = preco
        self.qtd = qtd
    
    def __str__(self):
        return(f"{self.id} - {self.name} - {self.preco} - {self.qtd}")
    
class SistemaEstoque():
    t_Estoque = []
        
    def cadastrarPeca(self):
        name = input("Qual o nome dessa peça? ")
        preco = input("Qual o preço da peça?")
        qtd = input("Quantas peças?")
        estoque = Estoque(len(self.t_Estoque), name, preco, qtd)
        self.t_Estoque.append(estoque)
        
    def listarPeca(self):
        for peca in self.t_Estoque:
            print(peca)
        
    def removerPeca(self):
        print("Para remover uma peça da lista, digite seu ID:")
        id = int(input("> "))
        self.t_Estoque.pop(int(id))
        
        

estoque = SistemaEstoque()

#Cadastrando 2 Peças
estoque.cadastrarPeca()
estoque.cadastrarPeca()
estoque.listarPeca()
estoque.removerPeca()
estoque.listarPeca()
