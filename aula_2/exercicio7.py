#Cálculo de desconto percentual

produto = float(input("Digite o valor do produto: "))
desconto = 10 /100
valor_desconto = produto * desconto
valor_final = produto - valor_desconto

print(f"O produto custa {produto} reais, o desconto fica {valor_desconto} reais, e o valor final deste produto fica {valor_final} reais!")