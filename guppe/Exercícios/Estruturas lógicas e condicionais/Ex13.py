"""
Faça um algoritmo que calcule a média ponderada de 3 provas. A primeira e a segunda prova têm peso 1 e a terceira prova
tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação
deve ser igual ou superior a 60 pontos.
"""

prova1 = int(input("Insira a nota da prova 1."))
prova2 = int(input("Insira a nota da prova 2."))
prova3 = int(input("Insira a nota da prova 3."))

media = (prova1 + prova2 + prova3 * 2) / 3
if media >= 60:
    print(f"A média do aluno é {media}. Está aprovado!")
else:
    print(f"A média do aluno é {media}. Está reprovado.")
