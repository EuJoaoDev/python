numeroSecreto = 10
descobriuNumero = False

for n in range(3):
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
else:
    print(f'Quase lá, o número secreto era {numeroSecreto}. Tente novamente!')