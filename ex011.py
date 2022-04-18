car_vendidos = float(input('quantos carros foram vendidos: '))
tot_vendas = float(input('qual o total de vendas: '))
sal_fixo = float(input('qual o salário fixo: '))
com_por_carro = float(input('qual a comissão que o funcionário recebe por carro: '))

print(f'O salário final é: {sal_fixo + com_por_carro + (tot_vendas*5/100)}')