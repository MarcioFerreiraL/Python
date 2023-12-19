from utilidadesCeV.moeda import moeda


def dado(num):
    type(num)
    if type(num) != int:
        print(f'ERRO: "{num}" não é um numero!')
        return False
    else:
        utilidadesCeV.moeda(num)
        return True
