# # #EXIBA OS NÚMEROS DE 1 A 10 USANDO LOOP WHILE
numeros = 1
while numeros <= 10:
    print(numeros)
    numeros += 1

# # Exercício 1: Use o range para imprimir os números de 1 a 10, um por linha.
# # (Dica: use um loop for com range)

for n in range(1, 11):
    print(n)


# # Exercício 2: Use um loop while para contar de 0 até 5 e imprimir os números.
# # (Dica: inicialize uma variável e incremente dentro do while)

numeros = 0
while numeros <=5:
    print(numeros)
    numeros+= 1


# # Exercício 3: Use range para imprimir todos os números pares de 2 a 20.
# # (Dica: o range pode pular de 2 em 2)

for n in range(2, 21, 2):
    print(n)


# Exercício 4: Use um loop while para pedir que o usuário digite números até que ele digite 0.
# (Dica: use input() e converta para int)

numeros = int(input("Digite um número (0 para sair): "))
while numeros != 0:
    print(f'Você digitou: {numeros}')
    numeros = int(input("Digite um número (0 para sair): "))
    
print('Loop acabou')
    

# Exercício 5: Use range para somar os números de 1 a 100 e imprimir o resultado final.
# (Dica: use uma variável acumuladora)

for n in range (1, 101):
    resultado = n + (n - 1) if n > 1 else n
    print(f'Soma acumulada até {n}: {resultado}')