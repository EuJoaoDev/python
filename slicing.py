# #slicing de sequências
# print("Slicing da lista:", lista[1:4])  # Exibe elementos do índice 1 ao 3
# print("Slicing da tupla:", alunos_tupla[1:4])  # Exibe elementos do índice 1 ao 3

# # explicação sobre slicing
# # Slicing é uma técnica que permite acessar uma parte de uma sequência, como listas ou tuplas.
# # Ele utiliza a notação [início:fim] para extrair uma sub-sequência de elementos.       
# # exemplo de slicing em uma string:
# print("Slicing da string:", texto[1:4])  # Exibe caracteres do índice 1 ao 3        
         

lista = [10, 20, 30, 40, 50, 60, 70, 80]
# a) Pegue os três primeiros elementos
# b) Pegue os três últimos
# c) Pegue os elementos nas posições ímpares
# d) Inverta a lista usando slicing

#a) 
lista [:3]

#b)
lista[-3:]

#c)
lista[::2]

#d)
lista[::-1]