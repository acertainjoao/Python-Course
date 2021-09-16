"""
Leia um número fornecido pelo utilizador. Se ess número for positivo, calcule a raiz quadrada desse número. Se o número
for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

numero = int(input('Insira um número.'))

if numero > 0:
    numero = numero ** 0.5
    print(f'{numero}')
else:
    print('O número é inválido')
