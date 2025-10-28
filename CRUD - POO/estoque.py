# Cadastro de peças finalizada

class Estoque:
    def __init__(self, id, name, preco, qtd):
        self.id = id
        self.name = name
        self.preco = preco
        self.qtd = qtd
    
    def __str__(self):
        return(f"{self.id} | Peça: {self.name} Preço UNI: R${self.preco} - Quantidade: {self.qtd}")
    
class SistemaEstoque():
    t_Estoque = []
        
    def cadastrarPeca(self):
        name = input("Nome da peça: ").upper()
        preco = input("Preço de custo: R$")
        qtd = int(input("Quantidade: " ))

        #Soma de quantidade
        existe = False                          #A Peça não existe por padrão
        for peca in self.t_Estoque:             #Ver todas as peças no estoque
            if peca.name == name:               #Se existir uma peça com o mesmo nome digitado na var name
                peca.qtd += qtd                 #Então some as quantidades
                existe = True                   #E a peça agora existe

        if not existe:                          #Se a peça não existir
            estoque = Estoque(len(self.t_Estoque), name, preco, qtd) #Crie uma nova instância
            self.t_Estoque.append(estoque)      #E adcione na lista

        
        
    def listarPeca(self):
        for peca in self.t_Estoque:
            print("-="*30)
            print(peca)
        
    def removerPeca(self):
        while True:
            print("Para remover uma peça da lista, digite seu ID (ou 'SAIR' para sair): ")
            id = int(input("> "))

            if id == 'SAIR': 
                print("Operação cancelada.")
                return
            
            for peca in self.t_Estoque:
                if id == peca.id:
                    opc = input(f"Tem certeza que quer excluir a peça {peca.name} [S/N]? ").strip().upper()
                    if opc == 'S':
                        self.t_Estoque.pop(id)
                        print('Peça removida')  
                    else:
                        print("Remoção cancelada.")
                    return  
            print("Essa peça não existe. Tente novamente.\n")

    def usarPeca(self):
        #Tratamento de erro + Baixa de peças
        while True:
            print("Para usar uma peça, digite seu ID (ou '0' para sair): ")

            id = int(input('> '))               #Digite o ID

            if id == '0':                       #Se for igual a 0
                print("Saindo...")              #Print "Saindo..."
                return                          #Saia do Metódo
            
            else:                                       #Se não
                for peca in self.t_Estoque:             #Para cada peça no estoque
                    if id == peca.id:                   #Se o ID existir no estoque
                        print(f'Peça: {peca.name} - Quantidade: {peca.qtd}') #Mostre o NOME e a QTD desse ID
                        quant = int(input('Quantas peças deseja usar? '))   #Pergunte quantas peças quer usar
                        if quant <= peca.qtd:                               #Se for menor que a quantidade
                            peca.qtd = peca.qtd - quant                     #Dê a baixa no pedido
                            print('Baixa concluída.')               
                        else:                                               #Se você digitou mais do que tem
                            print(f'Você não tem {quant} peças no estoque. Digite um valor válido') #Print
                        return
                    else:                               #Se o ID não existir
                        print('ID inválido.')           #Print

                    return
            
        
        

estoque = SistemaEstoque()

#Cadastrando 2 Peças
estoque.cadastrarPeca()
estoque.listarPeca()
estoque.usarPeca()
estoque.listarPeca()
