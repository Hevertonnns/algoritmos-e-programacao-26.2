#divisao de conta

porcao_de_frango= float(input("Qual o valor da porcao de frango? "))
refrigerante = float(input("Qual o valor da refrigerante? "))
pessoas = float(input("Há quantas pessoas para dividir? "))
volaorFinal= (porcao_de_frango + refrigerante) / pessoas
print (f"O valor da porção de frango custa {porcao_de_frango} reais, o refigerante custa {refrigerante} reais, para {pessoas} pessoas, fica extamente {volaorFinal:.2f}")