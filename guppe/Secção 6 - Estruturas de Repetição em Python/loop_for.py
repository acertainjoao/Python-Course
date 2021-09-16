"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java:

for(int i = 0; i < limitador; i++){
    //execução do loop
}

Pythn:

for item in iterável:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

#  Exemplo de for 1 (Iterando sobre uma string)
for letra in nome:
    print(letra)

#  Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

#  Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

Obs.: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)


Enumerate:

(0, 'G'), (1, 'e'), (2, 'e'), ...

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
Obs.: Quando não precisamos de um valor, podemo descartá-lo utilizando um '_'.

nome = 'Geek Univeristy'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos de transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    numero = int(input(f'Informe o valor {n}/{qtd}: '))
    soma = soma + numero
print(f'A soma é {soma}.')
"""

nome = 'Geek University'
for letra in nome:
    print(letra)
