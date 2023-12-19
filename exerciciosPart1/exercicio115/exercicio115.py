from utilidadesCeV.linha import linha
while True:
    linha.linhasF('Menu Principal')
    linha.linhas()
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    linha.linhas()
    x = int(input('Sua opção: '))
    linha.linhas()
    if x == 3:
        break
    elif x == 1:
        linha.lerArquivo('Nomes')
        if not linha.arquivoExiste('Nomes'):
            linha.criarArquivo('Nomes')
    elif x == 2:
        nome = input('Digite o nome:')
        idade = input('Digite a idade: ')
        linha.cadastrar('Nomes', nome, idade)
    else:
        print('error')