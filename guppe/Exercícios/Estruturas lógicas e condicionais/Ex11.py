"""
Escreva um programa que leia um número inteiro maior que zero e devolva, na tela, a soma de todos os algarismos. Por
exemplo, ao número 251 corresponderá o valor 8 (2+5+1). Se o número lido não for maior que zero, o programa terminará
com a mensagem 'Número inválido'.
"""

numero = int(input('Insira um número inteiro maior que zero à sua escolha.'))
res = 0

if numero <= 0:
    print('Número inválido.')
