salario = float(input('Digite o salário: '))
vendas = float(input('Digite o total de vendas: '))

if vendas > 1500:
	sal_total = salario+vendas*0.05
	print(f'O salário total é: {sal_total}')
else:
	sal_total = salario+vendas*0.03
	print(f'O salário total é: {sal_total}')