nascimento = int(input("informe o ano em que você nasceu: "))
ano_atual = int(input("informe o ano atual: "))

idade = ano_atual - nascimento
print(f'a sua idade e {idade}')

idade_meses = idade * 12
print(f'essa e sua idade em meses {idade_meses}')
 
idade_dias = idade * 365
print(f"essa e sua idade em dias {idade_dias}")