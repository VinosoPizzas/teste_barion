conta = int(input('digite o número da conta: '))
debito = float(input('digite o débito da conta: '))
credito = float(input('digite o crédito da conta: '))
saldo = float(input('digite o saldo da conta: '))
saldo_atual = saldo-debito+credito

if saldo_atual >= 0:
	print(f'Saldo positivo: {saldo_atual}')
else:
	print(f'Saldo negativo: {saldo_atual}')