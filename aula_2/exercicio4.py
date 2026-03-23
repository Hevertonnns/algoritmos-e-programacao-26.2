#consumo de conbustível

consumo_do_carro = int(input("Qual consumo do carro? k/l" ))
print(f"O consumo do carro é: {consumo_do_carro} km/l")

distancia_percorrida = int(input("Qual a distancia percorrida?"))
mes= 30
distancia_percorrida_por_mes= distancia_percorrida * mes
print (f"A distancia percorrida por mês é: {distancia_percorrida_por_mes} km")

gasolina = float(input("Qual o valor da gasolina?"))
litrosgastos = distancia_percorrida_por_mes / consumo_do_carro
valorgasto = gasolina * litrosgastos

print("O valor gasto é de: ", gasolina * litrosgastos)

