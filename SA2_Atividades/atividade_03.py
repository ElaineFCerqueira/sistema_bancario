'''
3. Escreva um programa que leia 20 valores inteiros e informe a média deles, o maior e o menor valor.

'''
import os
os.system ('cls||clear')

lista = []

for i in range(0,8):
    valor = int(input(f'Digite o {i+1}º valor: '))
    lista.append(valor)
print(f'A lista = {lista}')
media = sum(lista)/len(lista)
print(f'A media entre os valores é: {media}')
print(f'O maior valor é: {max(lista)}')
print(f'O menor valor é: {min(lista)}')