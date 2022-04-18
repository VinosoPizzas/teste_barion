macas_compradas = int(input('Quantas maças foram compradas: '))

if macas_compradas > 11:
	valor_maca = 1.0
else:
	valor_maca = 1.3

print(f'O valor total das maças é: R${macas_compradas*valor_maca}')