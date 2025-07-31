# valores = [83, 12, 47, 99, 3, 71, 56, 20, 34, 65]

# soma = 0
# for valor in valores:
#     soma += valor
#     print(f'a soma dos valores é {soma}')


# DADO UMA SEQUENCIA DE NUMEROS, CALCULE O MAIOR VALOR DA SEQUENCIA, NAO VALE USAR A FUNÇÃO MAX

# Lista de números inteiros
valores = [83, 12, 47, 99, 3, 71, 56, 20, 34, 65]

# Assume que o primeiro valor da lista é o maior inicialmente
maior = valores[0]

# Percorre cada número da lista
for valor in valores:
    # Se encontrar um valor maior que o atual "maior", atualiza a variável
    if valor > maior:
        maior = valor   

# Exibe o maior valor encontrado na lista
print(f'O maior valor da sequencia é {maior}')
