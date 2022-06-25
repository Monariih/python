from time import sleep
import os

'''  
Usada para escrever as frases iniciais no console
'''

'''
Uma linha separadora usada para dividir algumas expressões
'''


def separador():
    print('\033[34m-\033[m'*60)


'''
validador()
Valida que os caracteres digitados são binários, ou seja,
que contenham apenas "1" ou "0".
Se algum valor diferente de 0 ou 1 for encontrado, retorna falso
'''

'''
conversorDeBinarios()
CONVERSOR PRINCIPAL DA APLICAÇÃO
Recebe um numero binário, ja validado antes
Verifica o tamanho desse binario
Inverte o binario para fazer os calculos
Inicia um laço nesse numero
Verifica se a posição atual é "1"
Caso seja, aplica a as regras de potenciacao, usando o valor do index
Sempre somando isso ao valor decimal e acrescendo um ao index
Caso seja "0", não faz nada, só acresce ao index
Retorna o numero decimal obtido através dessas operações
'''


def conversorDeBinarios(valorBinario):
    index = 0
    decimal = 0
    tamanho = len(valorBinario) - 1  # Tamanho do binario digitado
    valorBinario = valorBinario[::-1]  # inverter todo o numero
    while index <= tamanho:
        if valorBinario[index] == "1":
            decimal += (2**index)
            index += 1
        else:
            decimal = decimal
            index += 1
    return decimal


def decimalParaBinario(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]


def validador(valoreInseridos):
    existeValorNaoBinario = True
    for i in list(valoreInseridos):
        if i != '1' and i != '0':
            existeValorNaoBinario = False
            break
    if not existeValorNaoBinario:
        print('\033[1;31mUm valor não binário foi inserido, digite somente 0 ou 1\033[m')
        sleep(1.4)
        print('Tentando novamente...')
        sleep(1.9)
    return existeValorNaoBinario


'''
leitor()
Executa os dois primeiros inputs e recebe os valores digitados
como STRING.
Envia esses valores ao validador(), caso este retorne falso,
exibe uma mensagem ao usuário e reinicia o leitor()
Valida se o usuário apertou o enter sem digitar nada.
Ao final disso, envia os valores já formatados como decimais
para a funcaoPrincipal()
'''


def leitor():
    os.system('cls') or None
    print('Vamos lá')
    separador()
    primeiroValorString = input("Insira o 1º valor:  ")
    if primeiroValorString == '':
        print('\033[1;31mVocê digitou um valor invalido.\033[m')
        sleep(1.3)
        print('Tentando novamente')
        sleep(1.0)
        leitor()

    segundoValorString = input("Agora insira o 2º valor:  ")
    if segundoValorString == '':
        print('\033[1;31mVocê digitou um valor invalido.\033[m')
        sleep(1.3)
        print('\033[1mTentando novamente\033[m')
        sleep(1.0)
        leitor()
    valoresEmConjunto = primeiroValorString+segundoValorString
    if validador(valoresEmConjunto):
        sleep(0.3)
        print("...")
        valorEmDecimal1 = conversorDeBinarios(primeiroValorString)
        valorEmDecimal2 = conversorDeBinarios(segundoValorString)
        sleep(0.5)
        separador()
        funcaoPrincipal(valorEmDecimal1, valorEmDecimal2,
                        primeiroValorString, segundoValorString)
    else:
        leitor()


'''
finalizar()
Método executado toda vez que o usuário solicita a finalização
da aplicação. Isso pode ocorrer pelo continuar() ou
funcaoPrincipal()
Exibe uma mensagem com intervalos de tempo sleep()
e encerra a execução do programa
'''


def finalizar():
    os.system('cls') or None
    sleep(0.5)
    print('Obrigado por usar nossa aplicação')
    separador()
    sleep(1.5)
    print('Até a próxima...')
    sleep(1.5)
    separador()
    sleep(1.5)
    
    print('\033[1;35mFeito pela eqp mais bonita da classe, Projetinho  Fellas\033[m')
    print('''
        __$$$$$___$$$$$$__ 
        _$$$$$$$_$$$$$$$$_ 
____Se a nota for boa Nois paga a coca____
        _$$$$$$$$$$$$$$$$_ 
        __$$$$$$$$$$$$$$__ 
        ____$$$$$$$$$$____ 
        _______$$$$_______ 
        ________$$________ ''')
    exit()


'''
continuar()
Solicita ao usuario a confirmação de continuação
caso receba "1", limpa o console e executa o leitor()
caso receba "2", executa o finalizar()
'''


def continuar():
    print('Quer realizar outra operação? \n1 - Sim \n2 - Não')
    outraOperacao = input('')
    if outraOperacao == '1':
        os.system('cls') or None
        leitor()
    elif outraOperacao == '2':
        finalizar()
    else:
        print("\033[1;31mDigite um valor válido...\033[m")
        sleep(1.2)
        print("Tentando novamente")
        sleep(1.2)
        separador()
        continuar()


'''
funcaoPrincipal
rebebe dois valores no formato decimal
*Solicita ao usuário a operação desejada
**Le o valor inserido pelo usuário, caso inválido executa novamente
***Verifica que o valor inserido é valido
****Mostra o resultado da operação de acordo com o valor selecionado
*****Ao final de qualquer operação, executa o continuar()
'''


def funcaoPrincipal(valor1, valor2, binario1, binario2):
    print('O 1º valor binário digitado foi: {} ele equivale a: {} em decimal. '.format(binario1, valor1))
    print('O 2º valor binário digitado foi: {} ele equivale a: {} em decimal. '.format(binario2, valor2))
    separador()
    print('''Qual operação você deseja realizar?
        Digite + para somar 
        Digite - para subtração
        Digite * para multiplicação
        Digite t para ver todos os resultados
        Digite s para sair''')
    separador()
    valorSelecionado = input("Insira o caracter da operação desejada: ")
    if valorSelecionado == "+":
        print("A soma de ", valor1, "+", valor2, "é: ", valor1 + valor2)
        print("O resultado em binário é: ",
              decimalParaBinario(valor1 + valor2))
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == "*":
        print("A multiplicação de ", valor1, "*",
              valor2, "é: ", valor1 * valor2)
        print("O resultado em binário é: ",
              decimalParaBinario(valor1 * valor2))
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == "-":
        print("A Subtração de ", valor1, "-", valor2, "é: ", valor1 - valor2)
        print("O resultado em binário é: ",
              decimalParaBinario(valor1 - valor2))
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == 't' or valorSelecionado == 'T':
        print('\033[1mTodos os resultados:\033[m ')
        print("A soma de ", valor1, "+", valor2, "é: ", valor1 + valor2)
        print("A soma em binário dará: ",
              decimalParaBinario(valor1 + valor2))
        print("A multiplicação de ", valor1, "*",
              valor2, "é: ", valor1 * valor2)
        print("A multiplicação em binário dará: ",
              decimalParaBinario(valor1 * valor2))
        print("A subtração de ", valor1, "/", valor2, "é: ", valor1 - valor2)
        print("A subtração em binário dará: ",
              decimalParaBinario(valor1 - valor2))
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == 's' or valorSelecionado == 'S':
        sleep(0.7)
        finalizar()
    else:
        print(
            """\033[1;31mVocê precisa selecionar uma das opções mostradas, vamos tentar novamente.\033[m""")
        sleep(2.6)
        print('\033[33m...Reiniciando...\033[m')
        sleep(1.4)
        print('\033[33m...\033[m')
        sleep(1.0)
        os.system('cls') or None
        funcaoPrincipal(valor1, valor2, binario1, binario2)


'#Inicio da execução'
leitor()