nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
        print(f'{nome}, você é maior de idade, pode entrar!')
        
else:
    print(f'{nome}, você é menor de idade, não pode entrar!')   