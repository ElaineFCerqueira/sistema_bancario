import os
os.system('cls||clear')

'''
a L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
a) tamanho da lista;
b) maior valor da lista;
c) menor valor da lista;
d) soma de todos os elementos da lista;
e) lista em ordem crescente;
f) lista em ordem decrescente.
g) sair
'''

lista=[5,7,2,9,4,1,3]

while True:
    print ('''
            a) tamanho da lista;
            b) maior valor da lista;
            c) menor valor da lista;
            d) soma de todos os elementos da lista;
            e) lista em ordem crescente;
            f) lista em ordem decrescente.
            g) sair
            ''')
    opcao = input('Digite a opção desejada: ')

    if opcao == 'a':
        print(f'A lista possue {len(lista)} elementos')

    if opcao == 'b':
        print(f' O maior valor da lista é o numero {max(lista)}')
    
    if opcao == 'c':
        print(f' O menor valor da lista é o numero {min(lista)}')

    if opcao == 'd':
        print(f' A soma dos elementos é: {sum(lista)}')
    
    if opcao == 'e':
        print(f' A lista em ordem crescente: {sorted(lista)}')
    
    if opcao == 'f':
        print(f' A lista em ordem decrescente: {sorted(lista,reverse=True)}')
    
    if opcao == 'g':
        print(f' Espero ter ajudado, volte sempre!')
        break

