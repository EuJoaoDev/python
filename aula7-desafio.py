#DESAFIO

# - pEDE PELO SEU NOME E IDADE
# - da oi para você
# - Conta quantas letras seu nome possui
# fala quantos anos você terá daqui a 5 anos

idade = input('Digite a sua idade: ')
nome = input('Digite o seu nome: ')
print('Olá, ' + nome + '!')

tamanhoNome = len(nome)
print('Seu nome possui ' + str(tamanhoNome) + ' letras.')

idadeFutura = int(idade) + 5
print('Daqui a 5 anos você terá ' + str(idadeFutura) + ' anos.')