h = float(input("informe sua altura: "))
sexo = input("informe o seu sexo: ")

# > maior >=maior ou igual
# < menor <= menor ou igual 
# == igual (comparação) != diferença 

#operadores logicos
#and (e -> &&) 
#or (ou -> )
#not (não -> !)

if sexo == "m" or sexo == 'M':
  peso = (72.7 * h) - 58
  print(f'esse e seu peso ideal {peso:.3f}')

elif sexo == 'f' or sexo == 'F' :
    peso = (62.1 * h) - 44.7
    print(f'esse e seu peso ideal {peso:.3f}')
else : 
   print('sexo invalido')