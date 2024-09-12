numeros = []
    
while True:
    numero = float(input("informe o numero (digite 0 caso queira parar): "))
    if numero == 0:
        break
    else:
        numeros.append(numero)
soma = 0    
for i in numeros:
    soma += i 
    #soma = soma + i

soma2 = sum(numeros)
print(f'utilizando a função sum: {soma2}')              
media = soma / len(numeros)
quantidade = len(numeros)
print(f'a soma dos numeros e {soma}')
print(f'a media dos numeors e {media}')
print(f'a quantidade de elementos e {quantidade}') 
