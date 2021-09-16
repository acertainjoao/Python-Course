"""
Leia um número real. Se o número for positivo, imprima a raiz quadrada. Se for negativo, imprima o número ao quadrado.
"""

numero = float(input('Insira um número real à sua escolha.'))

if numero > 0:
    numero = numero ** 0.5
    print(numero)
else:
    numero = numero ** 2
    print(numero)
