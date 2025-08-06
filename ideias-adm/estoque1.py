#Alerta simples de estoque baixo
etq = int(input('Quantos estoque há disponível?'))
minimo = 5
if etq < minimo:
    print('Alerta! faça a reposição dos estoques!')
else:
    print('Estoque ok')