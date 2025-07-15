# Exercício 1 – Hello World
# Escreva um programa que exiba "Hello World!" na tela usando a função print.

print('Hello World!')


# Exercício 2 – Números com Python
# Crie duas variáveis com números inteiros.
# Calcule e exiba: a soma, subtração, multiplicação, divisão e potência entre eles.

numero1 = 10
numero2 = 50

numero1 + numero2  # Soma
numero1 - numero2  # Subtração  
numero1 * numero2  # Multiplicação
numero1 / numero2  # Divisão

print(f' soma é: {numero1 + numero2}')
print(f' subtração é: {numero1 - numero2}')
print(f' multiplicação é {numero1 * numero2 }')
print(f' divisão é: {numero1 / numero2}')
print(f' potência é: {numero1 ** numero2}')

# Exercício 3 – Textos, conversão e concatenação
# Peça ao usuário seu nome e sua idade.
# Converta a idade para inteiro e diga quantos anos ele terá no ano seguinte.

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
idade = int(idade)  # Convertendo a idade para inteiro

print(f'Olá {nome}, obrigado por me avisar que tem {idade} anos! No próximo ano você terá {idade + 1} anos. ')


# Exercício 5 – Variáveis
# Declare variáveis para o nome de uma pessoa, idade e profissão.
# Mostre esses dados formatados em uma frase.

nome = 'João'
idade = 27
profissão = "Engenheiro de software"
print(f' meu nome é {nome}, tenho {idade} anos e sou {profissão}!')

# Exercício 6 – Input
# Solicite do usuário dois números com `input()`, some-os e exiba o resultado.
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número')

print(f' A soma dos dois número é { num1 + num2 }')

# Exercício 7 – F-string
# Use f-string para criar uma mensagem como:
# "João tem 25 anos e trabalha como programador."

nome = 'João'
idade = 27
profissão = "Programador"
print(f' meu nome é {nome}, tenho {idade} anos e sou {profissão}!')


# Exercício 8 – Controle de Fluxo (if, elif, else)
# Peça ao usuário um número inteiro e diga se ele é positivo, negativo ou zero.
numero = int(input('Digite um número inteiro: '))   
if numero > 0:
    print('O número é positivo.')   
elif numero < 0:
    print('O número é negativo.')   
else:
    print('O número é zero.')


