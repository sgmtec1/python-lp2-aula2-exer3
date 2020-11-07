'''
Preencha uma lista com 10 números sorteados aleatóriamente. A partir desta lista, gere uma lista com os números pares e outra lista com os números ímpares.
Exemplo:
Suponha que a lista com os números sorteados seja: 
[1, 4, 7, 9, 5, 3, 7, 9, 8, 8].
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]

'''

import random

lista = []

for i in range(10):
    n = random.randint(1,50) # entre 1 e 50
    lista.append(n)

print('Números sorteados: ', lista)

pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('Números sorteados pares: ', pares)
print('Números sorteados impares: ', impares)
