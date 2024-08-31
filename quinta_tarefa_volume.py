raio = float(input("informe o raio do recipiente: "))
altura = float(input("informe a altura do recipiente: "))
#primeira forma
volume = 3.141590 * raio * raio * altura

#segunda forma
volume2 = 3.141590 * raio **2 * altura

#terceira forma
import math
volume3 = math.pi * math.pow(raio, 2) * altura


print(f'o volume do seu recipiente e {volume:.2f}')