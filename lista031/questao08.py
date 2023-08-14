'''
8)	Fazer um programa que calcule e apresente a quantidade de litros que um
automóvel gastará em uma viagem. O programa deve coletar as seguintes
informações:
- Distância a percorrer na viagem, em quilômetros;
- qual é o valor do consumo médio do automóvel, em quilômetros por litro.
'''

distancia = float(input("Distância a percorrer na viagem, em quilômetros: "))
consumo_medio = float(input("Qual é o valor do consumo médio do automóvel, em quilômetros por litro? "))

litros = distancia / consumo_medio

print(f"O seu carro vai consumir {litros:.0f} litros de combustível.")
