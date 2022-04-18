v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))
v3 = float(input('Insira o terceiro valor: '))

if v1==v2 or v1==v3 or v2==v1 or v2==v3:
	print('ERRO: os valores são iguais')
else:
	valores = [v1,v2,v3]
	valores.sort()
	maior_valor = max(valores)
	
	print(maior_valor)

	