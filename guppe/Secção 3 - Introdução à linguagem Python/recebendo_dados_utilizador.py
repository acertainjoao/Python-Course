"""
Recebendo dados do utilizador

input() -> Todos os dados recebidos via input são do tipo String.

Em Python, String é tudo o que estiver entre:
- Aspas simples
- Aspas duplas
- Aspas simples triplas
- Aspas duplas triplas

Exemplos:
- Aspas simples -> 'João'
- Aspas duplas -> "João"
- Aspas simples triplas -> '''João'''
"""
# Aspas duplas triplas -> """João"""

# Entrada de dados
# print("Qual o seu nome?")
# nome = input()

nome = input("Qual o seu nome?")

# Exemplo de print "antigo" (versão 2.x)
# print("Seja bem vindo(a) %s." % nome)

# Exemplo de print "antigo" (versão 2.x)
# print("Seja bem vindo(a) {0}.".format(nome))

# Exemplo de print "mais atual" (versão a partir da 3.7)
print(f"Seja bem vindo(a) {nome}.")

# print("Qual a sua idade?")
# idade = input()

idade = int(input("Qual a sua idade?"))

# Processamento

# Saída de dados

# Exemplo de print "antigo" (versão 2.x)
# print("A %s tem %s anos." % (nome, idade))

# Exemplo de print "antigo" (versão 3.x)
# print("A {0} tem {1} anos.".format(nome, idade))

# Exemplo de print "mais atual" (versão a partir da 3.7)
print(f"O/A {nome} tem {idade} anos.")

print(f"O/A {nome} nasceu em {2021 - idade}.")
"""
int(idade) -> cast 

Cast é a "conversão" de um tipo de dado para outro.
"""