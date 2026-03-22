#circuferência
import math

raio= int(input("Digite o raio de um circulo: "))
Diametro = 2*raio
Area = math.pi*(raio**2)
perimetro = math.pi*Diametro
print (f" O raio é {raio}, valaor do Diametro é {Diametro}, e a area é {Area:.2f}, e o perimetro é {perimetro:.2f}")
