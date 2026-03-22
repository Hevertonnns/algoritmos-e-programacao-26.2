nome = input("Digite seu nome: ")
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_futuro = int(input("Digite o ano de futuro: "))

idade = ano_futuro - ano_nasc
print(f"{nome}, no ano {ano_futuro}, voce tera {idade} anos.")
