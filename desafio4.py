# Esse é o número mágico que a gente quer que a pessoa adivinhe.
numeroSecreto = 10

# Aqui dizemos que, no começo do jogo, ninguém acertou o número ainda.
descobriuNumero = False

# PRIMEIRA CHANCE
# Se a pessoa ainda não descobriu o número, ela pode tentar adivinhar.
if not descobriuNumero:
    tentativa = int(input("Digite um número: "))  # A pessoa digita um número

    # Se ela chutou um número maior que o número secreto...
    if tentativa > numeroSecreto:
        print("O número é maior que o número secreto.")  # ... avisamos que passou!

    # Se ela chutou um número menor que o número secreto...
    elif tentativa < numeroSecreto:
        print("O número é menor que o número secreto.")  # ... avisamos que está abaixo!

    # Se ela acertar o número certinho...
    else:
        print("Parabéns! Você acertou o número secreto.")  # ... damos os parabéns!
        descobriuNumero = True  # E marcamos que ela acertou o número.

# SEGUNDA CHANCE
# Se ela ainda não acertou, damos mais uma tentativa.
if not descobriuNumero:
    tentativa = int(input("Digite um número: "))

    if tentativa > numeroSecreto:
        print("O número é maior que o número secreto.")
    elif tentativa < numeroSecreto:
        print("O número é menor que o número secreto.")
    else:
        print("Parabéns! Você acertou o número secreto.")
        descobriuNumero = True

# TERCEIRA CHANCE
# Última tentativa se ainda não acertou nas duas anteriores.
if not descobriuNumero:
    tentativa = int(input("Digite um número: "))

    if tentativa > numeroSecreto:
        print("O número é maior que o número secreto.")
    elif tentativa < numeroSecreto:
        print("O número é menor que o número secreto.")
    else:
        print("Parabéns! Você acertou o número secreto.")
        descobriuNumero = True

# DEPOIS DAS 3 TENTATIVAS
# Agora vamos ver se a pessoa conseguiu ganhar ou não.
if descobriuNumero:
    print("E também, ganhou o jogo!.")  # Se acertou, ela venceu!
else:
    print(f'Quase lá, o número secreto era {numeroSecreto}. Tente novamente!')  # Se não acertou, mostramos o número.
