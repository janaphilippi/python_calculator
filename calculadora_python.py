# Calculadora em Python

print('************* Calculadora em Python *************')
print('                     by Jana \n\n')
print('    Olá! Seja bem vindo à minha calculadora!!! \n\n\n')
print('Sabendo que esta calculadora oferece as seguintes opções:\n')

terminador = False
while terminador == False:

    print('1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão \n ')


    operacao = int(input('Escolha qual operação deseja realizar (1, 2, 3 ou 4): '))
    # print(operacao)

    lista_operacoes = [1, 2, 3, 4]
    verificador = False


    if operacao in lista_operacoes:
        verificador = True

    while verificador == False:
        correcao = int(input('Esta operação não está catalogada. Por favor, escolha um número entre 1 e 4: '))
        if correcao in lista_operacoes:
            operacao = correcao
            verificador = True
        else:
            verificador = False


    op_escolhida = '\n%s'
    if operacao == 1:
        string = 'SOMA'
    elif operacao == 2:
        string = 'SUBTRAÇÃO'
    elif operacao == 3:
        string = 'MULTIPLICAÇÃO'
    elif operacao == 4:
        string = 'DIVISÃO'
    print(op_escolhida%string)


    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    # print('\n')

    def soma(x, y):
        resultado = x + y
        return resultado

    def subt(x, y):
        resultado = x - y
        return resultado

    def mult(x, y):
        resultado = x * y
        return resultado

    def div(x, y):
        resultado = x / y
        return resultado


    if operacao == 1:
        print('O resultado da sua soma é: ', soma(num1, num2), '\n')
    elif operacao == 2:
        print('O resultado da sua subtração é: ', subt(num1, num2), '\n')
    elif operacao == 3:
        print('O resultado da sua multiplicação é: ', mult(num1, num2), '\n')
    elif operacao == 4:
        print('O resultado da sua divisão é: ', div(num1, num2), '\n')

    terminator = False
    while terminator == False:
        nova_op = input('\nVocê deseja realizar uma nova operação? Sim ou Não? ')
        if nova_op == 'sim' or nova_op == 'Sim' or nova_op == 'yes':
            terminador = False
            terminator = True
            print('\nQual operação você deseja fazer?')
        elif nova_op =='não' or nova_op == 'nao' or nova_op == 'Não' or nova_op == 'no':
            terminador = True
            terminator = True
        else:
            print ('\nNão te entendi muito bem!:(')
            print('Repetirei a pergunta. Preste atenção, por favor!')
            terminator = False
print('\nMuito obrigada e volte sempre!\n')
