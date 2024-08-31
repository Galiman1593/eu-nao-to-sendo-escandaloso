valor_da_hora = float(input("informe o valor que você recebe por hora: "))

horas_de_aula = float(input("informe quantas horas de aula você da por mês: "))

descontos = float(input("quanto por mês e descontado de seu salario por mês: ")) 

salario = (valor_da_hora * horas_de_aula) - descontos

print(f'o seu dalario total mensal sera {salario:.2f}')

