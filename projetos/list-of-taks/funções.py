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
        cabecalho('LISTA DE TAREFAS')
        coisas = []
        coisas = task.readlines()

        for pos, tasks in enumerate(coisas):
            tasks = tasks.replace(';', '')
            tasks = tasks.replace('\n', '')
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


def deletar_tarefa(nome_arquivo):
    try:
        with open(nome_arquivo, 'rt') as task:
            cabecalho('Lista das Tarefas')
            coisas = task.readlines()
            for pos, tasks in enumerate(coisas):
                tasks = tasks.replace(';', '')
                tasks = tasks.replace('[] -', '')
                tasks = tasks.replace('\n', '')
                print(f'{pos + 1} - {tasks}')
            print('-' * 50)
            print('Qual você quer excluir? ')
            print('OBS: Digite a numeração da task.')
            num = int(input())
            for pos, tasks in enumerate(coisas):
                if num - 1 == pos:
                    tasks = tasks.replace('\n', '')
                    confirmation = ''
                    while confirmation != 'N':
                        print(f'"{tasks}" essa é a task que você escolheu.')
                        confirmation = input('Tem certeza que você quer excluir essa task? ').strip().upper()[0]
                        if confirmation == 'S':
                            frase = tasks
                            break
                        elif confirmation == 'N':
                            return False
                        else:
                            print('Digite [S/N].')
        nome_arquivo_temporario = 'arquivo_temporario.txt'
        with open(nome_arquivo, 'r') as arquivo_original, open(nome_arquivo_temporario, 'w+') as arquivo_temporario:
            linhas = arquivo_original.readlines()
            for linha in linhas:
                if linha.strip() != frase:
                    arquivo_temporario.write(linha)
        import os
        nome_arquivo = 'sqlite.txt'
        os.remove(nome_arquivo)
        os.rename(nome_arquivo_temporario, nome_arquivo)
        return True
    except IOError as e:
        print(f'Erro ao manipular o arquivo: {e}')
        return False