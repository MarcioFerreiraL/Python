def converter(numero, base):
    if base == 1:
        return bin(numero)
    elif base == 2:
        return oct(numero)
    elif base == 3:
        return hex(numero)
    else:
        return "Base inválida. Escolha 1 para binário, 2 para octal ou 3 para hexadecimal."

numero = int(input("Digite um número inteiro: "))
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Digite a opção desejada (1/2/3): "))

if opcao in [1, 2, 3]:
    resultado = converter(numero, opcao)
    print(f"O número {numero} na base {opcao} é: {resultado}")
else:
    print("Opção inválida. Escolha entre 1, 2 ou 3 para a base de conversão.")
