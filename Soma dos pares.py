soma = 0
cont = 0
for c in range(1, 11):
    num = int(input('Escreva um numero: '))
    if num % 2 == 0:
        soma = soma+1
        cont = cont+1
print('Voce informou 10 numeros e entre esses foram escolhidos {} numeros pares'.format(cont, soma))
