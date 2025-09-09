# numero = (int(input("Digite um númmero: ")))
# if numero >=0:print('f O número é positivo')
# else:print('O número é negativo')

# numero = (int(input("Digite um númmero: ")))
# if numero % 2 ==0:
#     print('O número é par')
# else:
#     print('O número é ímpar')


# idade = (int(input("Digite sua idade: ")))

# if idade <= 12:
#     (print("Você é uma criança"))
# elif idade >12 and idade <18:
#     (print("Você é um adolescente"))
# elif idade >=18 and idade <64:
#     (print("Você é um adulto"))
# else:
#     (print("Você é um idoso"))

# senha = "joao12345"
# senha_digitada = input("Digite sua senha: ")
# if senha_digitada == senha:
#     print("Acesso permitido")
# else:
#     # print("Acesso negado")


##### AND, OR, NOT E IS #####

#AND - PARA QUE FUNCIONE TUDO PRECISA SER VERDADEIRO
#OR - PARA QUE FUNCIONE APENAS UM PRECISA SER VERDADEIRO   
#NOT - INVERTE O VALOR BOOLEANO, SE FOR TRUE FICA FALSE E VICE VERSA
#IS - COMPARA SE UM OBJETO É IGUAL AO OUTRO

# ativo = True
# logado = True

# if ativo and logado:
#     print("Bem-vindo ao sistema")
# else:
#     print("Você precisa logar sua conta. Por favor, verifique seu e-mail")
    
# if ativo or logado:
#     print("Bem-vindo ao sistema")   
# else:
#     print("Você precisa ativar sua conta. Por favor, verifique seu e-mail")
    
# if not ativo:
#     print("você precisa ativar sua conta. Por favor, verifique seu e-mail")
# else:
#     print("Bem-vindo ao sistema")
    
# if ativo is True:
#     print("Bem-vindo ao sistema")
    
# if logado is False:
#     print("Você precisa logar sua conta. Por favor, verifique seu e-mail")
    
# if ativo is not True:
#     print("Você precisa ativar sua conta. Por favor, verifique seu e-mail")
    
# if ativo is True and logado is True:
#     print("Bem-vindo ao sistema")

idade = (int(input("Digite sua idade: ")))

if idade >= 13 and idade <= 19:
    print("Você é um adolescente")
    
nome_dia_semana = input("Digite o nome do dia da semana: ").lower()
if nome_dia_semana == "sábado" or nome_dia_semana == "domingo":
    print("É fim de semana!")
else:
    print("É dia de semana!")
    
    senha = input("Digite uma senha: ")
    tem_numero = any(char.isdigit() for char in senha)
    tem_maiuscula = any(char.isupper() for char in senha)

    if len(senha) > 8 and (tem_numero or tem_maiuscula):
        print("Senha forte")
    else:
        print("Senha fraca")
        
numero = int(input("Digite um número: "))
if numero is not > 0:
    print("O número é positivo")
else:
    print("O número é negativo")
    

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista4 = lista1

if lista1 is lista2:
    print("As listas são iguais")

if lista1 is lista3:
    print("As listas são iguais")