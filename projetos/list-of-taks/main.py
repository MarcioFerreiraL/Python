import funções
from time import sleep
while True:
    titulo = 'Tasks'
    funções.cabecalho(titulo.upper())
    topicos = ['Listar Tarefas', 'Cadastrar Tarefa', 'Excluir Tarefa / Concluir Tarefa', 'Sair do sistema']
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
                nome = input('Digite a tarefa: ').strip()
                funções.criarTask('sqlite.txt', nome)
            case 3:
                print('Indisponivel...')
            case 4:
                print('Obrigado e até mais :)!')
                break
            case _:
                print('error!')
                print('Digite algum dos numeros que estão na tabela.')