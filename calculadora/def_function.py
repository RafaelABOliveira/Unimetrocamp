import util

operacao = input('Digite sem pontuação ou acentos o que você quer fazer: ')
num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))

if operacao == 'soma':
    total = print("Total = {}".format(util.soma(num1,num2)))

elif operacao == 'subtracao':
    total = print("Total = {}".format(util.subtracao(num1,num2)))

elif operacao == 'multiplicacao':
    total = print("Total = {}".format(util.multiplicacao(num1,num2)))

elif operacao == 'divisao':
    total = print("Total = {}".format(util.divisao(num1,num2)))

else: 
    print('Operação inválida')
