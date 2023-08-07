'''
10)	Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso,
 utilizando a fórmula
 prestação = valor + (valor x (taxa : 100) x tempo em dias).

 Perfuntar ao usuário:
 - valor normal da prestação
 - taxa de juros
 - tempo em dias

 resposta:
 - valor da prestação em atraso
'''

valor = float(input("Qual o valor normal da prestação? "))
taxa = float(input("Qual a taxa de juros? "))
tempo = float(input("Quantos dias de atraso? "))

#  prestação = valor + (valor x (taxa : 100) x tempo em dias).
prestacao = valor + (valor * (taxa / 100) * tempo)

print("O valor da prestação em atraso é R$", prestacao)



