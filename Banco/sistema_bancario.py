import os
os.system('cls||clear')

saldo = 0
limite = 500
limite_saque = 3
numero_saque = 0
extrato = []
deposito = []
saque = []


print('''========= SISTEMA BANCÁRIO ==========
      1 - Depósito
      2 - Saque
      3 - Extrato
      4 - Sair
======================================''')
while True:
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        dinheiro = int(input('Digite o valor a depositar: R$ '))
        if dinheiro > 0:
            deposito.append(dinheiro)
            print(f'Valor de R$ {dinheiro} depositado com sucesso ')
        else:
            print('Digite um valor válido, tente novamente')
    
    if opcao == 2:
        valor_saque = int(input("Digite o valor a ser sacado: R$ "))
        saque.append(valor_saque)

        if valor_saque > limite:
            print(f'Tente novamente, Seu limite de saque é de {limite}')
        
        elif valor_saque > sum(deposito):
            print('Você não saldo suficiente')
        
        elif numero_saque >= limite_saque:
            numero_saque+=limite_saque
            print('Você execeu o limite diário de saques')

        else:
            novo_valor = sum(deposito) - valor_saque
            print('Saque registrado, aguarde a contagem das cedulas')
    
    if opcao == 3:
        print(f' Seu saldo é R$ {novo_valor:.2f}')

        print(f'O valor sacado foi R$ {sum(saque):.2f}')
    
    if opcao == 4:
        print('Obrigada!, volte sempre.')
        break


    
         


