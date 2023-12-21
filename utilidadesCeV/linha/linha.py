def linhasF(frase):
    x = len(frase)
    print('-' * (x + 14))
    print(f'  {frase.upper().center(len(frase) + 10)}  ')
    print('-' * (x + 14))
def linhas():
    print('-' * (28))

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um ERROR na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        linhas()
        print(f'PESSOAS CADASTRADAS')
        linhas()
        print(a.read())
        b = 0
        for dado in a:
            dado[b] = dado [b].replace(';', ' - ')
            dado[b] = dado [b].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            b += 1
    finally:
        a.close()
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        task = open(arq, 'at')
    except:
        print('Houve algum ERRO na abertura do arquivo!')
    else:
        try:
            task.write(f'{nome};{idade}\n')
        except:
            print(f'Houve algum ERRO na hora de escrever os dados em {arq}')
        else:
            print('Novo registro adicionado.')