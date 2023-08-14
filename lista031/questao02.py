'''
2)	Elaborar um programa que pergunte quatro valores inteiros e apresente
2 resultados:
a)	Resultado de suas adições
b)	Resultado de suas multiplicações
'''

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))
num4 = int(input("Informe o quarto número: "))

soma = num1 + num2 + num3 + num4
mult = num1 * num2 * num3 * num4

print(f"A soma dos 4 números inseridos é {soma}.")
print(f"A multiplicação dos 4 números inseridos é {mult}.")