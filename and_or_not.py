# Pergunta se a pessoa está com fome e verifica a resposta.
# Se a resposta for 's', 'tenhoFome' será True, caso contrário, será False.
tenhoFome = input('Estou com fome? (Digite s para sim): ') == 's'

# Pergunta se a pessoa tem comida em casa e verifica a resposta.
# Se a resposta for 's', 'tenho_comida' será True, caso contrário, será False.
tenho_comida = input('Tenho comida em casa? (Digite s para sim:) ') == 's'  

# Verifica se a pessoa está com fome e NÃO tem comida em casa.
# Se for verdade, ele executa o código abaixo.
if tenhoFome and not tenho_comida:
    print('Preciso ir ao mercado')  # Sugere que a pessoa vá ao mercado comprar comida
    print('Voltar para casa')  # Depois de comprar, a pessoa deve voltar para casa
    print('Preparar uma refeição')  # A pessoa deve preparar uma refeição
    print('Comer')  # Depois de preparar, a pessoa pode comer

# Verifica se a pessoa está com fome e TEM comida em casa.
# Se for verdade, ele executa o código abaixo.
if tenhoFome and tenho_comida:
    print('Preparar uma refeição')  # A pessoa pode preparar a refeição já que tem comida
    print('Comer')  # E depois comer
