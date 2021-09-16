"""
Escopo de variáveis

/<--------- Escopo --------->/

Dois casos de escopo:

1) Variáveis globais;
   - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.
2) Variáveis locais.
   - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja,
   seu escopo está limitado ao bloco onde foi declarada.

Para declarar variávies em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica.
Isso significa que. ao declararmos uma variável, não colocamos o tipo dela, este é
inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existe = 'Oi'
print(nao_existe)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada localmente dentro do bloco do if.
    print(novo)

print(novo)
