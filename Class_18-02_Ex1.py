#Find the bigger and smaller number in a list

lista_numeros = []
#contador = 0
#maior_valor = 0
#menor_valor = 0
novo_valor = True

while novo_valor:
    numero = int(input('Qual o valor? '))
    lista_numeros.append(numero)
    flag = input('Continua (y/n)? ')
    if flag != 'y':
        novo_valor = False

# for index_numero in lista_numeros:
#     if index_numero == lista_numeros[0]:
#         maior_valor = index_numero
#         menor_valor = index_numero
#     else:
#         if maior_valor < index_numero:
#             maior_valor = index_numero
#         if menor_valor > index_numero:
#             menor_valor = index_numero

print(lista_numeros)
print('O maior valor é: ', max(lista_numeros)) #métodos max e min 
print('O menor valor é: ', min(lista_numeros))