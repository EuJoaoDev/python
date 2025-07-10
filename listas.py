# Exemplos de listas em Python

# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Criando uma lista de strings
frutas = ["maçã", "banana", "laranja"]

# Criando uma lista misturada (com diferentes tipos de dados)
misturada = [1, "texto", 3.14, True, [10, 20]]

# Adicionando elementos à lista
frutas.append("uva")

# Acessando elementos da lista
primeira_fruta = frutas[0]  # "maçã"

# Removendo elementos da lista
frutas.remove("banana")

# Iterando sobre uma lista
for fruta in frutas:
    print(fruta)

# Tamanho da lista
tamanho = len(frutas)
print("Quantidade de frutas:", tamanho)

# Iterando sobre a lista misturada
print("Elementos da lista misturada:")
for elemento in misturada:
    print(elemento)