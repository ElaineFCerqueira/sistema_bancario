'''
Faça um programa que leia 4 valores,
calcule a média e imprima positivo ou negativo 
(para ser positivo a média deve ser acima de 1).
'''

import os
os.system('cls||clear')

lista = []

for i in range(0,4):
    numero = float(input(f'Digite o {i+1}º numero: '))
    lista.append(numero)

media = sum(lista)/len(lista)
if media >= 1:
    print(f'Média:{media} = Positivo')
else: 
    print(f'Média:{media} = Negativo')

    