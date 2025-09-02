texto = input("Insira um texto:")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(f'Deste texto, a(s) vogal(is) encontrada(s) foi(ram): {letra.upper()}')
    else:
        print(f'Deste texto, a(s) consoante(s) encontrada(s) foi(ram): {letra.upper()}')
        
        
        
for n in range(0,11,2):
    print(n)