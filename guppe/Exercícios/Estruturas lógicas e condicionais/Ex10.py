"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre o seu peso ideal, utilizando as seguintes
fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 78
    - Mulheres: (61.2 * h) - 44.7
"""

altura = float(input('Insira a sua altura (em metros).'))
sexo = input('Insira o seu sexo (M/F).')
peso_ideal = 0

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'O seu peso ideal é {peso_ideal}')
elif sexo == 'F':
    peso_ideal = (61.2 * altura) - 44.7
    print(f'O seu peso ideal é {peso_ideal}')
