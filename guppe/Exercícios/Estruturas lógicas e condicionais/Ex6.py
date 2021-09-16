"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente
entre ambos.
"""

num1 = int(input('Insira o primeiro número.'))
num2 = int(input('Insira o segundo número.'))
dif = 0

if num1 > num2:
    print(f'{num1}')
    dif = num1 - num2
    print(f'{dif}')
elif num1 < num2:
    print(f'{num2}')
    dif = num1 - num2
    print(f'{dif}')
