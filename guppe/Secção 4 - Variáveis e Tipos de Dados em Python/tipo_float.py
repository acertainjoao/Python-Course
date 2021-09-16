"""
Tipo Float aka Tipo real, Tipo decimal

Casas decimais

Obs.: o separador de casas decimais na programação é o ponto e não a vírgula.
"""

# Errado do ponto de vista float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
Obs.: ao converter valores floats para inteiro, perdemos precisão
"""
resultado = int(valor)
print(resultado)
print(type(resultado))

# Podemos trabalhar com números complexos
var = 5j
