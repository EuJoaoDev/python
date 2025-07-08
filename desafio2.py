# Início do programa, avisamos que começamos
print("Início")

# Perguntamos para a pessoa se ela está com fome
fome = input("Você está com fome? (sim/não): ")

# Se a resposta for "sim", a pessoa está com fome
if fome == 'sim':
    # Então perguntamos se tem comida em casa
    comida = input('Você tem comida? (sim/não): ')

    # Se a resposta for "não", ou seja, não tem comida em casa...
    if comida == 'não':
        # ...a pessoa precisa ir ao mercado
        print('ir ao mercado')
        # ...depois precisa voltar para casa
        print('voltar para casa')
        # ...aí ela pode preparar a comida
        print('preparar uma refeição')
        # ...e por fim, comer!
        print('comer')
    else:
        # Se a resposta foi "sim", ou seja, tem comida em casa
        # Então é só preparar a refeição...
        print('preparar uma refeição')
        # ...e comer!
        print('comer')
else:
    # Se a pessoa não está com fome, o programa acaba aqui
    print('fim')
