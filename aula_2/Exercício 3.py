#conversao de tempo

minutos = int(input("Digite um valor em minutos: "))

hora = minutos // 60
minutosrestantes = minutos % 60
print(f"{minutos} minutos,  equivalem a {hora} hora's', e sobram {minutosrestantes} minutos")