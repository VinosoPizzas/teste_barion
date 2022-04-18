v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))

if v1 == v2:
	print('ERRO: insira valores diferentes')
elif v1 > v2:
	print('O primeiro valor é maior')
else:
	print('O segundo valor é maior')