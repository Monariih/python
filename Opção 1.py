num = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTADECIMAL
[3] converter para HEXADECIMAL
[4] exibir o resultado das 3 operações''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif opção == 2:
    print('{} convertido para OCTADECIMAL é igual a {}'.format(num, oct(num)[2:]))

elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

elif opção == 4:
    print('O resultado das 3 operações é igual a: ')
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
    print('{} convertido para OCTADECIMAL é igual a {}'.format(num, oct(num)[2:]))
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('opção invalida, tente novamente')