'''
Crie um programa que converta horas em segundos, conforme o valor que o usuário informar quando solicitado a ele.
'''

import os
os.system('cls||clear')

def conversor_horas():
    segundos = horas*60
    print(f'{horas} horas, equivalem a {segundos} segundos')

horas = int(input('Digite as horas: '))
conversor_horas()