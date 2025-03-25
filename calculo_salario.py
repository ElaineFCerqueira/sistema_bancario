#crie um sistema de recebe o salario bruto feito na contratação 
# sabendo que o trabalhador não recebe o total nfi salario bruto e sim o salario liquido
#calcule o salario liquido baseado nesses critérios

import os
os.system('cls||clear')

print('-'*40)
print('CALCULO DE SALÁRIO')
print('-'*40)

# Solicitar o valor do salario bruto
salario_bruto = float(input('Digite o valor do salario: R$ '))

# Calculo para o imposto de renda
ir = (18/100)*salario_bruto

# Calculo para o INSS
INSS = (5/100)*salario_bruto

# Calculo no auxilio familia com base na quantidade de filhos
quantidade_filhos = int(input('Você tem filhos?, quantos? (Em caso negativo, digite 0) '))
auxilio_familia = quantidade_filhos * 35

# Calculo  para o salario líquido
salario_liquido = salario_bruto - ir - INSS + auxilio_familia

print('-'*40)
print(f'A dedução do imposto de renda será R$ {ir}')
print(f'A dedução do INSS será de R$ {INSS}')
print(f'O auxilio familia será de R$ {auxilio_familia}')
print('-'*40)
print(f'O salário bruto é de R$ {salario_bruto}, após a dedução dos impostos o salário liquido será de: R$ {salario_liquido}')

