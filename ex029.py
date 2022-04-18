v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))
v3 = float(input('Insira o terceiro valor: '))

valores = [v1, v2, v3]
valores.remove(min(valores))

print(f'A soma dos dois maiores valores é: {valores[0]+valores[1]}')