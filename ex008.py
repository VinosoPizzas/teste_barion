votos_brancos = int(input('digite o total de votos brancos: '))
votos_nulos = int(input('digite o total de votos nulos: '))
votos_validos = int(input('digite o total de votos válidos: '))
eleitores = votos_brancos+votos_validos+votos_nulos

if votos_brancos < 0:
	print('votos brancos imcompatíveis.')
elif votos_nulos < 0:
	print('votos nulos imcompatíveis')
elif votos_validos < 0:
	print('votos válidos imcompatíveis')
else:
	print(f'Dos {eleitores} votos feitos pelos eleitores, {int(100*(votos_nulos/eleitores))}% foram nulos')
	print(f'{int(100*(votos_brancos/eleitores))}% foram brancos')
	print(f'e {int(100*(votos_validos/eleitores))}% foram válidos')


"""votos_brancos = votos_brancos * eleitores / 100
votos_nulos = votos_nulos * eleitores / 100
votos_validos = votos_validos * eleitores / 100"""



# print(f'Porcentagem de votos nulos: {100 * (votos_nulos/eleitores)}')