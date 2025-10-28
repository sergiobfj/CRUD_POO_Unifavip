import clientes, estoque, servicos, relatorio
from time import sleep
import os

    # Aqui vai ser o menu principal. 
def espera():
    os.system("cls")
    print("Aguarde", end='', flush=True)  # imprime "Aguarde" e mantém na mesma linha
    for _ in range(3):
        sleep(0.5)
        print('.', end='', flush=True)  # adiciona os pontos
    print()  # pula para a próxima linha depois dos pontos

    
def menu_principal():
    while True:
        print('\n=-=-=-= BEM-VINDO AO SISTEMA =-=-=-=')
        print('[1] Gerenciar Cliente')
        print('[2] Gerenciar Peça')
        print('[3] Gerenciar Serviço')
        print('[4] Gerar Relatório')
        print('[0] Sair')

        opcao = input('Escolha uma opção: ')
      
        if opcao == "1":
            espera()
            menu_clientes()
        elif opcao == "2":
            espera()
            menu_pecas()
        elif opcao == "3":
            espera()
            menu_servico()
        elif opcao == "4":
            espera()
            menu_relatorio()
        elif opcao == "0":
            espera()
            print('Saindo do sistema...')
            break
        else:
            espera()
            print('Opção inválida! Tente novamente.')

    # Aqui vai ser o menu do cliente. Você vai gerencia-lo por aqui.
def menu_clientes():
    sistema_clientes = clientes.SistemaClientes()
    while True:
        print('\n=-=-=-= GERENCIAR CLIENTES =-=-=-=')
        print('[1] Cadastrar Cliente')
        print('[2] Listar Clientes')
        print('[3] Remover Cliente')
        print('[0] Voltar ao menu principal')

        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            espera()
            sistema_clientes.cadastrarCliente()
        elif opcao == "2":
            espera()
            sistema_clientes.listarCliente()
        elif opcao == "3":
            espera()
            sistema_clientes.removerCliente()
        elif opcao == "0":
            break
        else:
            espera()
            print('Opção inválida!')

    # Aqui vai ser o menu das peças. Organize as peças por aqui. 
def menu_pecas():
    sistema_estoque = estoque.SistemaEstoque()
    while True:
        print('\n=-=-=-= GERENCIAR PEÇAS =-=-=-=')
        print('[1] Adicionar Peça')
        print('[2] Listar Peças')
        print('[3] Remover Peça')
        print('[0] Voltar ao menu principal')

        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            espera()
            sistema_estoque.adicionarPeca()
        elif opcao == "2":
            espera()
            sistema_estoque.listarPeca()
        elif opcao == "3":
            espera()
            sistema_estoque.removerPeca()
        elif opcao == "0":
            break
        else:
            espera()
            print('Opção inválida!')

    # Aqui vai ser o menu de serviços.
def menu_servico():
    sistema_servico = servicos.SistemaServicos()
    while True:
        print('\n=-=-=-= GERENCIAR SERVIÇOS =-=-=-=')
        print('[1] Cadastrar Serviço')
        print('[2] Listar Serviços')
        print('[3] Remover Serviço')
        print('[0] Voltar ao menu principal')

        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            print('Qual serviço deseja cadastrar?')
            espera()
            sistema_servico.cadastroServico()
        elif opcao == "2":
            print('Qual serviço deseja listar?')
            espera()
            sistema_servico.listarServicos()
        elif opcao == "3":
            print('Qual serviço deseja remover?')
            espera()
            sistema_servico.removerServico()
        elif opcao == "4":
            print("Qual serviço você quer atualizar?")
            espera()
            sistema_servico.atualizarStatus()
        elif opcao == "0":
            print('Voltando ao menu principal...')
            espera()
            break
        else:
            print('Opção inválida!')

    # Aqui vai ser o menu de relatórios.
def menu_relatorio():
    sistema_relatorio = relatorio.sistemaRelatorios()
    while True:
        print('\n=-=-=-= GERAR RELATÓRIOS =-=-=-=')        
        print('[1] Relatório de Serviços')
        print('[2] Relatório de Peças')
        print('[0] Voltar ao menu principal')
       
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print('Gerando relatório de serviços...')
            espera()
            sistema_relatorio.relatorioDeServicos()
        elif opcao == '2':
            print('Gerando relatório de peças...')
            espera()
            sistema_relatorio.relatorioDeServicos()
        elif opcao == '0':
            print('Voltando ao menu principal...')
            espera()
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    menu_principal()
