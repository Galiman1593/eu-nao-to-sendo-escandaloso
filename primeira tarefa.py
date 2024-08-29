
valor_total = float(input("informe o valor total da compra: "))
parcelas = int(input("informe o total de parcelas: "))

divisao = valor_total / parcelas

print(f'o valor total da compra foi {valor_total}, você escoleu parcelar em {parcelas} parcelas, o valor das parcelas sera {divisao:.2f}')