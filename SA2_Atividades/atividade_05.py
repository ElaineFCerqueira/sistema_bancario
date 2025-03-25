'''
Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve
imprimir todos os elementos da lista, enumerando-os.

'''

import os
os.system('cls||clear')

def criar_lista(lista):
    for i in range (0,10):
        valor = int(input('Digite o numero: '))
        lista.append(valor)
    print(lista)
    print(f'{i+1}º - {valor}')
  


lista = []
criar_lista(lista)