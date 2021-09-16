"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário,
imprima: 'Empréstimo não concedido', caso contrário, imprima: 'Empréstimo concedido'.
"""

salario = float(input('Insira o valor do seu salário.'))
prestacao = float(input('Insira o valor da prestação.'))

if prestacao > salario * 0.20:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
