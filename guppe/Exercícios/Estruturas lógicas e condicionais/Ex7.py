"""
Faça um programa que receba dois números e mostre o maior. Se, por acaso, os dois números forem iguais, imprima a
mensagem 'Números iguais'.
"""

num1 = input('Insira o primeiro número.')

num2 = input('Insira o segundo número.')

if num1 > num2:
    print(f'{num1}')
elif num1 < num2:
    print(f'{num2}')
else:
    print('Números iguais.')
