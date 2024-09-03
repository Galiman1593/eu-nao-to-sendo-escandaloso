nadador = int(input("informe sua idade: "))
if nadador >= 5 and nadador <= 7: 
    print("infantil A")
    
elif nadador >= 8 and nadador <= 10:
    print("infantil B")
   
elif nadador >= 11 and nadador <= 13:
    print("juvenil A")   

elif nadador >= 14 and nadador <= 17:
    print("juvenil B")   

elif nadador >= 18:
    print("adulto")  
else :
    print("essa idade não corresponde")
