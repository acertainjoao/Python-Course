"""
Tipo Booleano

Álgebra Booleana criada por George Boole

2 constantes: Verdadeiro ou Falso (True ou False em Python)

Obs.: Sempre com a inicial maiúscula.
Errado: true, false
Certo: True, False
"""

ativo = False
print(ativo)

"""
Operações básicas:
"""
# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso e vice-versa.
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binária, ou seja , depende de dois valores. Ou um ou outro devem ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
