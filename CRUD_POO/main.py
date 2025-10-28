import clientes
import estoque

    # Aqui vai ser o menu principal. 
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
            menu_clientes()
        elif opcao == "2":
            menu_pecas()
        elif opcao == "3":
            menu_servico()
        elif opcao == "4":
            menu_relatorio()
        elif opcao == "0":
            print('Saindo do sistema...')
            break
        else:
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
            sistema_clientes.cadastrarCliente()
        elif opcao == "2":
            sistema_clientes.listarCliente()
        elif opcao == "3":
            sistema_clientes.removerCliente()
        elif opcao == "0":
            break
        else:
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
            sistema_estoque.adicionarPeca()
        elif opcao == "2":
            sistema_estoque.listarPeca()
        elif opcao == "3":
            sistema_estoque.removerPeca()
        elif opcao == "0":
            break
        else:
            print('Opção inválida!')

    # Aqui vai ser o menu de serviços.
def menu_servico():
    while True:
        print('\n=-=-=-= GERENCIAR SERVIÇOS =-=-=-=')
        print('[1] Cadastrar Serviço')
        print('[2] Listar Serviços')
        print('[3] Remover Serviço')
        print('[0] Voltar ao menu principal')

        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            print('Qual serviço deseja cadastrar?')
        elif opcao == "2":
            print('Qual serviço deseja listar?')
        elif opcao == "3":
            print('Qual serviço deseja remover?')
        elif opcao == "0":
            print('Voltando ao menu principal...')
            break
        else:
            print('Opção inválida!')

    # Aqui vai ser o menu de relatórios.
def menu_relatorio():
    while True:
        print('\n=-=-=-= GERAR RELATÓRIOS =-=-=-=')        
        print('[1] Relatório de Clientes')
        print('[2] Relatório de Peças')
        print('[0] Voltar ao menu principal')
       
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print('Gerando relatório de clientes...')
        elif opcao == '2':
            print('Gerando relatório de peças...')
        elif opcao == '0':
            print('Voltando ao menu principal...')
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    menu_principal()
