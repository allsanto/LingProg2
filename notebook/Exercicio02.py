# 1 Crie um programa que recebe uma lista de números e
# retorne o maior elemento
# retorne a soma dos elementos
# retorne o número de ocorrências do primeiro elemento da lista
# retorne a média dos elementos
# retorne o valor mais próximo da média dos elementos
# retorne a soma dos elementos com valor negativo
# retorne a quantidade de vizinhos iguais
# (a += b) é uma abreviação para a = a + b

# lista2 = []
# for c in range (0, 5):
#     lista2.append(int(input(f'Digite um valor para a Posição {c}:')))
#     print('=-' * 30)
#     print(f'Você digitou os valores {lista2}')
    
# nmaior = lista2[0]
# nsoma = 0
# nocorre = 0
# nsomaneg = 0
# nqtdb = 0
# a = lista2[0] + 1

# for n1 in lista2:
#     if n1 > nmaior:
#         nmaior = n1
#     nsoma += n1
#     if n1 == lista2[0]:
#         nocorre += 1    
#     if n1 < 0:
#         nsomaneg += n1
#     if n1 == a:
#         nqtdb += 1
#     a = n1
#     media = nsoma / len(lista2)
#     maisProximo = lista2[0]
# diferenca = media - lista2[0]
# menorDiferenca = diferenca
# for n1 in lista2:
#     diferenca = media - n1
#     if diferenca < 0:
#         diferenca = diferenca * -1
#     if diferenca < menorDiferenca:
#         menorDiferenca = diferenca
#         maisProximo = n1
            
# print("Maior elemento: ", nmaior)
# print("Soma dos elementos: ", nsoma)
# print("Numero de ocorrências de elementos %i: %i:" % (lista2[0], nocorre))
# print("Média dos elementos: ", media)
# print("Numero mais proximo da média: ", maisProximo)
# print("Soma dos Elementos Negativos: ", nsomaneg)
# print("Vizinhos iguais: ", nqtdb)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------


# 2 Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrario.
# Duas listas são iguais se possuem os mesmos valores e na mesma ordem.

# lista1 = []
# for a in range (0, 5):
#     lista1.append(int(input(f'Digite um valor para posição {a} da Lista01:')))
#     print('=-' * 30)
# lista2 = []
# for b in range (0, 5):
#     lista2.append(int(input(f'Digite um valir para posição {b} da Lista02:')))
#     print('=-' * 30)

# def listaIguais(lista1, lista2):
#     if len(lista1) == len(lista2):
#         for i in range(0, len(lista1)):
#             if lista1[i] != lista2[i]:
#                 return False
#         return True
#     return False
# print('=-' * 30)
# print(f'Os valores digitados da lista 1 são: {lista1} ')
# print(f'Os valores digitados da lista 2 são: {lista2} ')
# print("As lista são iguais?", listaIguais(lista1, lista2))

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# 3 Faça um programa que receba duas listas e retorne True se têm os mesmos
# elementos ou False caso contrário
# Duas listas possuem os mesmos elementos quando são compostas pelos mesmos
# valores, mas não obrigatoriamente na mesma ordem.

# lista1 = []
# for a in range (0, 5):
#     lista1.append(int(input(f'Digite um valor para posição {a} da Lista01:')))
#     print('=-' * 30)
# lista2 = []
# for b in range (0, 5):
#     lista2.append(int(input(f'Digite um valir para posição {b} da Lista02:')))
#     print('=-' * 30)

# def listaIguais(lista1, lista2):
#     lista1.sort()
#     lista2.sort()
#     if len(lista1) == len(lista2):
#         for i in range(0, len(lista1)):
#             if lista1[i] != lista2[i]:
#                 return False
#         return True
#     return False
# print('=-' * 30)
# print(f'Os valores digitados da lista 1 são: {lista1} ')
# print(f'Os valores digitados da lista 2 são: {lista2} ')
# print("As lista são iguais?", listaIguais(lista1, lista2))

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# 4 Faça um programa que percorre uma lista com o seguinte formato:
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]].
# Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:
# O programa deve imprimir na tela.
# -O total de faltas do campeonato
# -O time que fez mais faltas
# -O time que fez menos faltas

jogos = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

tfaltas = 0
for np in jogos:
    tfaltas += np[2][0]
    tfaltas += np[2][1]

f = {}
for np in jogos:
    f[np[0]] = 0
    f[np[1]] = 0

for np in jogos:
    f[np[0]] += np[2][0]
    f[np[1]] += np[2][1]

print(f'Resultado dos Jogos: {jogos}')
print('=-' * 30)
print(f'Total de Faltas: {tfaltas}')
print('=-' * 30)
print(f'Time com mais faltas: {max(f, key=f.get)} - {f[max(f, key=f.get)]} faltas')
print('=-' * 30)
print(f'Time com menos faltas: {min(f, key=f.get)} - {f[min(f, key=f.get)]} faltas')