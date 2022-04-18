custo_carro = float(input('Digite o custo de fábrica do carro: '))
per_distribuidor = float(custo_carro*28/100)

# imposto = roubo

roubos = float(custo_carro*45/100)


print(f'O preço final do carro é: {custo_carro+per_distribuidor+roubos}')