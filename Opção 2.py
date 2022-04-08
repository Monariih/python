print('Bem vindo ao conversor de BINARIO para DECIMAL, HEXADECIMAL, OCTADECIMAL.')

num = input('Digite um BINARIO para realizar a conversão: ')

print('''Escolha uma base para a conversão
[1] converter para DECIMAL
[2] converter para HEXADECIMAL
[3] converter para OTADECIMAL
[4] exibir todos os resultados''')

opção = int(input('Sua opção: '))

if opção == 1:
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) *2**n
        n = n -1
    print(f'O BINARIO convertido para DECIMAL é igual a {decimal}.')

elif opção == 2:
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) *2**n
        n = n -1
    print('o BINARIO {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(decimal)[2:]))

elif opção == 3:
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) *2**n
        n = n -1
    print('o BINARIO {} convertido para OCTADECIMAL é igual a {}'.format(num, oct(decimal)[2:]))

elif opção == 4:
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) *2**n
        n = n -1
    print(f'O BINARIO convertido para DECIMAL é igual a {decimal}.')
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) *2**n
        n = n -1
    print('o BINARIO {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(decimal)[2:]))
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) *2**n
        n = n -1
    print('o BINARIO {} convertido para OCTADECIMAL é igual a {}'.format(num, oct(decimal)[2:]))

else:
    print('Tente novamente saco de pancreas.')