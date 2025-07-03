# Exemplos básicos de f-strings em Python

nome = "Maria"
idade = 25

# Exemplo 1: Inserindo variáveis em uma string
mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)

# Exemplo 2: Expressões dentro de f-strings
print(f"No ano que vem, {nome} terá {idade + 1} anos.")

# Exemplo 3: Formatando números
preco = 19.99
print(f"O preço do produto é R$ {preco:.2f}")

# Exemplo 4: Usando dicionários
dados = {"produto": "Livro", "quantidade": 3}
print(f"Você comprou {dados['quantidade']} unidades de {dados['produto']}.")

# Exemplo 5: Chamando funções dentro de f-strings
def saudacao(nome):
    return f"Bem-vindo(a), {nome}!"

print(f"{saudacao('João')}")