from time import sleep

while True:
    import funções
    titulo = 'Tasks'
    funções.cabecalho(titulo.upper())
    topicos = ['Listar Tarefas', 'Cadastrar Tarefa', 'Excluir Tarefa', 'Sair do sistema']
    funções.corpo(topicos)
    escolha = input('Sua opção: ')
    if escolha.isdigit() == False:
        print('error!')
        print('Digaite algum dos numeros que estão na tabela.')
    else:
        escolha = int(escolha)
        match escolha:
            case 1:
                nameBD = 'sqlite.txt'
                check = funções.checarBancodeDados(nameBD)
                if check is not True:
                    print('Banco de Dados não encontrado :(')
                    funções.criarBancodeDados(nameBD)
                    print('Criando banco de dados...')
                    sleep(2)
                    print('Banco de dados criado com sucesso! :)')
                funções.lerTask(nameBD)
            case 2:
                while True:
                    nome = input('Digite a tarefa: ').strip()
                    funções.criarTask('sqlite.txt', nome)
                    confirmador = input('Quer cadastrar outra task? [S/N]').strip().upper()[0]
                    if confirmador == 'N':
                        break
                    elif confirmador == 'S':
                        print('OK!')
                        sleep(1)
                    else:
                        print('Digite Sim ou Não.')
            case 3:
                nameBD = 'sqlite.txt'
                funções.deletar_tarefa(nameBD)

            case 4:
                print('Obrigado e até mais :)!')
                break
            case _:
                print('error!')
                print('Digite algum dos numeros que estão na tabela.')
