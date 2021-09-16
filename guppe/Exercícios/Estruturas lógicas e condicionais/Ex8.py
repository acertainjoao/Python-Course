"""
Faça um programa que leia duas notas de um aluno, verifique se as notas são válidas e exiba na tela a média dessas
notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor
válido, este facto deve ser informado ao utilizador e o programa termina.
"""

nota1 = float(input('Insira a nota do primeiro aluno.'))
nota2 = float(input('Insira a nota do segundo aluno.'))
media = 0

if nota1 > 10.0 or nota2 > 10.0:
    print('Uma ou ambas as notas são inválidas.')
else:
    media = (nota1 + nota2)/2
    print(f'A média das notas é {media}')
