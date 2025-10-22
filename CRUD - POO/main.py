import os
import clientes
import estoque

print("Seja bem vindo ao Cleitinho Assistant")
os.system('cls')
while True:
    print("Observe as opções abaixo: \n1 - Cadastrar Peça\n2 - Cadastrar Cliente\n3 - Listar Estoque\n4 - Listar Clientes\n5 - Sair")
    opcao = input("Digite a opção que deseja: ")
    if opcao == 1:
        clientes.SistemaClientes()
        clientes.cadastrarClientes()
        