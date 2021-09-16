"""
Faça um programa que receba dois números e mostre qual qual deles é o maior.
"""

print('Insira o primeiro número.')
num1 = input()

print('Insira o segundo número.')
num2 = input()

if num1 > num2:
    print(f'{num1} é maior do que {num2} ')
elif num1 < num2:
    print(f'{num2} é maior do que {num1}')
else:
    print('Os números são iguais.')
