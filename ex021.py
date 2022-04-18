print('Use modelos 24 horas e apenas números inteiros(sem os minutos)')
hr_inicio = int(input('insira a hora de início: '))
hr_final = int(input('insira a hora em que o jogo acabou: '))
hrs_jogo = 0

if hr_inicio == hr_final:
	print('Tempo máximo de duração atingido!')
	hrs_jogo = 24
elif hr_final >= hr_inicio:
	hrs_jogo = hr_final-hr_inicio
else:
	hrs_jogo = (24-hr_inicio)+hr_final

print(f'A partida durou {hrs_jogo} horas')
