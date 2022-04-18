qnt_estoque = int(input('Digite a quantidade presente em estoque: '))
qnt_max = int(input('Digite a quantidade máxima em estoque: '))
qnt_min = int(input('Digite a quantidade mínima em estoque: '))
qnt_media = (qnt_max+qnt_min)/2

if qnt_estoque > qnt_media:
	print(f'Não efetuar compra, quantidade em estoque: {qnt_estoque}')
else:
	print(f'Efetuar compra, quantidade em estoque: {qnt_estoque}')	