sal_atual = float(input('digite o salário atual: '))
per_reajuste = float(input('digite a porcentagem de reajuste: '))

print(f'O salário passara de {sal_atual} para {(sal_atual*per_reajuste/100)+sal_atual}')