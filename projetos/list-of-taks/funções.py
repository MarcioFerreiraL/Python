def cabecalho(frase):

    print('-' * (50))
    print(f'  {frase.center(50)}  ')
    print('-' * (50))

def corpo(frase):
    for pos, frases in enumerate(frase):
        print(f'{pos+1} - {frases.upper()}')
    print('-' * (50))

def checarBancodeDados(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True
def criarBancodeDados(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um ERROR na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')

def lerTask(nome):
    try:
        task = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('Lista das Tarefas')
        coisas = []
        coisas.append(task.read())
        print()
        for pos, tasks in enumerate(coisas):
            tasks = tasks.replace(';', '')
            print(f'{tasks}')
        task.close()


def criarTask(arq, nome):
    try:
        task = open(arq, 'at')
    except:
        print('Houve algum ERRO na abertura do arquivo!')
    else:
        try:
            task.write(f'[] - {nome}; \n')
        except:
            print(f'Houve algum ERRO na hora de escrever os dados em {arq}')
        else:
            print('Novo registro adicionado.')
        finally:
            task.close()