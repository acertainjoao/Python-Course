"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - o número inserido ao quadrado;
    - a raiz quadrada do número inserido
"""

numero = float(input('Insira um número à sua escolha.'))

if numero > 0:
    numero = numero ** 2
    numero = numero ** 0.5
    print(numero)
