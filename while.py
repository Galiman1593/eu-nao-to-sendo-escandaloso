#ler indeterminados numeros 
#a condição eo usuario responder 'n' para a pergunta "deseja continuar? (s/n)"
soma = 0 
while True:
    numero = int(input("informe o numero: "))
    r = input("deseja continuar? (s/n)")
    soma = soma + numero
    if r == 'n' or r == 'N':
        break
    print(f'a soma e {soma}')