<<<<<<< HEAD
def verifica_parenteses(expressao):
    pilha = []

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha or pilha[-1] != '(':
                return False
            pilha.pop()

    return not pilha  # A expressão está balanceada se a pilha estiver vazia no final

# Recebe a expressão do usuário
expressao = input("Digite a expressão com parênteses: ")

# Verifica se os parênteses estão balanceados
if verifica_parenteses(expressao):
    print("Os parênteses estão balanceados.")
else:
=======
def verifica_parenteses(expressao):
    pilha = []

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha or pilha[-1] != '(':
                return False
            pilha.pop()

    return not pilha  # A expressão está balanceada se a pilha estiver vazia no final

# Recebe a expressão do usuário
expressao = input("Digite a expressão com parênteses: ")

# Verifica se os parênteses estão balanceados
if verifica_parenteses(expressao):
    print("Os parênteses estão balanceados.")
else:
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
    print("Os parênteses não estão balanceados.")