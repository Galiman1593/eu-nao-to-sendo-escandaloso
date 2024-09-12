#{mais comuns: array, vetor}, {quase nunca visto: conjunto}, {nome apenas visto em java: coleção}(em java), sao a mesma coisa. todos são listas

#numero = 5
#print(type(numero))
#numero.append(7)
#dara erro porque não existe o metodo "append" na classe int

#declarando uma lista
vetor = []
vetor.append(5)
vetor.append(7)
print(type(vetor)) # o type e importante para saber a classe da variavel 
print(vetor)

vetor.append(4.3)
vetor.append('renato')
print(vetor)
print(f'quantidade de elementos {len(vetor)}') #len vc consegue descobrir a quantidade de elementos na sua lista 
# primeira posição começa com 0 (zero)
print(vetor[0])

for i in vetor:
    print(i)
