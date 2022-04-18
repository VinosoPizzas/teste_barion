hrs_trabalhadas = int(input('quantas horas foram trabalhadas no mês: '))
sal_hora = float(input('quantos são recebidos por hora: '))
hrs_semanais = hrs_trabalhadas/4
sal_final = hrs_trabalhadas*sal_hora

if hrs_semanais <= 40:
	print(sal_final)
else:
	sal_final = sal_final+(hrs_semanais-40)*(sal_hora*50/100)
	print(sal_final)