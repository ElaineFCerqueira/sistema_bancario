import os
os.system('cls||clear')

'''
A proposta de avaliação que desenvolveremos juntos é fornecer à pessoa os tipos de empréstimo adequados para ela, dadas algumas variáveis:

Devemos fornecer os seguintes tipos de empréstimo:

Empréstimo Pessoal. Taxa de Juros: 4%
Empréstimo com garantia. Taxa de juros: 3%.
Empréstimo Consignado. Taxa de Juros: 2%
Abaixo estão listadas as regras comerciais para concessão de empréstimo com base no perfil da pessoa:

Empréstimo Pessoal	Empréstimo Colateralizado	Folha de pagamento
Renda <= 3000	Sim	Sim***	Não
Renda > 3000 e < 5000	Sim	Sim**	Não
Renda => 5000	Sim	Sim*	Sim
* Clientes com menos de 30 anos
** Clientes residentes em SP (código do estado de São Paulo no Brasil)
*** Clientes menores de 30 anos residentes em SP

'''


def verificar_emprestimo(renda,idade,estado):
    if renda <=3000 and estado == 'SP' and idade < 30:
        print('Empréstimo com garantia. Taxa de juros: 3%, sem desconto em folha')
    elif renda > 3000 and renda < 5000 and idade < 30:
        print('Empréstimo com garantia. Taxa de juros: 3%, sem desconto em folha')
    elif renda >= 5000 and idade < 30:
        print('Empréstimo Consignado. Taxa de Juros: 2%, desconto em folha')
    else:
        print('Empréstimo Pessoal. Taxa de Juros: 4%')
    


nome = input('Digite o seu nome: ')
cpf = int(input('Digite seu CPF (sem pontos, sem traços)'))
idade = int(input('Digite a sua idade: '))
estado = input('Digite a cidade(sigla): ').strip().upper()
renda = float(input('Digite a sua renda líquida: '))

verificar_emprestimo(renda,idade,estado)

  