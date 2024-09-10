#4) O cardápio de uma lanchonete é o seguinte:
#Especificação	Código	Preço
#Cachorro quente	100	1,20
#Bauru simples	101	1,30
#Bauru com ovo	102	1,50
#Hambúrger	103	1,20
#Cheeseburguer	104	1,30
#Refrigerante	105	1,00
#Escrever um programa que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche.
#A cada iteração deve perguntar se o usuário deseja continuar, a resposta for igual a 'n', o programa encerrará a execução.
# No final, deverá ser apresentado o valor total. 
#101 = 1.20
total = 0

while True:
    codigo = float(input("informe o codigo do pedido: "))
    quantidade = int(input("informe a quantidade: "))
    preco = 0.00
    if codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.30
    elif codigo == 105:
        preco = 1.00                    
    total = total + (preco * quantidade)
    

    r = input("deseja continuar? (s/n)")
    if r == 'n' or r == 'N':
        break

print(f'o valor sera {total:.2f}')
    