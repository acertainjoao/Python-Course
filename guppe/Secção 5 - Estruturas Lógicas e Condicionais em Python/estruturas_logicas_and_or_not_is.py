"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam de ser True.
Para o 'or', um ou outro valor precisa de ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se for True, passa a False e vice-versa.

"""
ativo = True
logado = False

if ativo:
    print('Bem-vindo!')
else:
    print('Precisa de ativar a sua conta. Por favor, verifiquee oo seu e-mail!')


# ativo é True?
print(ativo is True)
