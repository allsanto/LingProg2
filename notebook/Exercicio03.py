Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
  print(f'O maior numero é {num1}')
else:
  print(f'O maior numero é {num2}')


/*-----------------------------------------------------------------------------------------------------*/
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogais = ['a','e','i','o','u']
letra = input('Digite uma letra: ').lower()

if letra in vogais:
  print(f'{letra} é vogal.')
else:
  print(f'{letra} é consoante.')
 
 /*-----------------------------------------------------------------------------------------------------*/
 
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media == 10:
  print('Aprovado com Distinção.')
elif media >= 7:
  print('Aprovado')
else:
  print('Reprovado')

/*-----------------------------------------------------------------------------------------------------*/
Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1 >= num2 and num1 >= num3:
  maior = num1
  if num2 >= num3:
    meio = num2
    menor = num3
  else:
    meio = num3
    menor = num2
elif num2 >= num1 and num2 >= num3:
  maior = num2
  if num1 >= num3:
    meio = num1
    menor = num3
  else: 
    meio = num3
    menor = num1
else:
  maior = num3
  if num2 >= num1:
    meio = num2
    menor = num1
  else:
    meio = num1
    menor = num2

print(maior, meio, menor)

/*-----------------------------------------------------------------------------------------------------*/
5.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-salários até 280,00 (incluindo) : aumento de 20%.
-salários entre 280,00 e 700,00 : aumento de 15%
-salários entre 700,00 e 1500,00 : aumento de 10%
-salários de 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste;
-o percentual de aumento aplicado;
-o valor do aumento;
-o novo salário, após o aumento.


salario = float(input('Digite o salario atual: '))

if salario <= 280:
  percent = 20
elif salario > 280 and salario < 700:
  percent = 15
elif salario >= 700 and salario < 1500:
  percent = 10
else:
  percent = 5
  
aumento = salario*(percent/100)

print(f'Salário inicial: {salario}',
      f'\nPercentual de aumento aplicado: {percent}%', 
      f'\nValor do aumento: {aumento}',
      f'\nNovo salário: {salario+aumento}')
	  
	  
/*-----------------------------------------------------------------------------------------------------*/
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input('Digite um numero: '))

if num == 1:
  dia= 'Domingo'
elif num == 2:
  dia= 'Segunda-Feira'
elif num == 3:
  dia= 'Terça-Feira'
elif num == 4:
  dia= 'Quarta-Feira'
elif num == 5:
  dia= 'Quinta-Feira'
elif num == 6:
  dia= 'Sexta-Feira'
elif num == 7:
  dia= 'Sábado'
else:
  dia= 'Valor inválido'

print(dia)


/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento Conceito Entre 9.0 e 10.0 A Entre 7.5 e 9.0 B Entre 6.0 e 7.5 C Entre 4.0 e 6.0 D Entre 4.0 e zero E O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media >= 9.0 and media <= 10:
  conceito = 'A'
  msg = 'APROVADO'
elif media >= 7.5 and media < 9.0:
  conceito = 'B'
  msg = 'APROVADO'
elif media >= 6.0 and media < 7.5:
  conceito = 'C'
  msg = 'APROVADO'
elif media >= 4.0 and media < 6.0:
  conceito = 'D'
  msg = 'REPROVADO'
elif media >= 0 and media < 4.0:
  conceito = 'E'
  msg = 'REPROVADO'

print(f'NOTA 1 = {n1} NOTA 2 = {n2}',
       f'\nMÉDIA = {media}',
       f'\nCONCEITO: {conceito}',
       f'\n{msg}')
	   
	   
/*-----------------------------------------------------------------------------------------------------*/
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
-Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
-Triângulo Equilátero: três lados iguais;
-Triângulo Isósceles: quaisquer dois lados iguais;
-Triângulo Escaleno: três lados diferentes;


l1 = int(input('Primeiro lado: '))
l2 = int(input('Segundo lado: '))
l3 = int(input('Terceiro lado: '))

if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
  if l1 == l2 and l2 == l3 and l1 == l3:
    print('Triângulo Equilátero')
  elif l1 == l2 or l2 == l3 or l1 == l3:
    print('Triângulo Isósceles')
  else:
    print('Triângulo Escaleno')
else:
  print('Não é um triângulo')
  
/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
-Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
-Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
-Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
-Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input('Informe o valor de A: '))

if a==0:
  print('Equação não é de 2°Grau.')
else:
  b = int(input('Informe o valor de B: '))
  c = int(input('Informe o valor de C: '))
  delta = (b*b)-(4*a*c)
  if delta < 0:
    print('A equação não possui raízes reais.')
  elif delta == 0:
    x = ((-b) + (delta ** 0.5))/2*a
    print(f'A equação possui apenas uma raiz real: {x}')
  else:
    x1 = ((-b) + (delta ** 0.5))/2*a
    x2 = ((-b) - (delta ** 0.5))/2*a
    print(f'A equação possui duas raízes reais: {x1} e {x2}')
	
/*-----------------------------------------------------------------------------------------------------*/
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
-Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
-Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


val = int(input("Digite o valor: "))

if val >= 10 and val <= 600:
    n100 = val // 100
    resto = val % 100
    print(f'{n100} notas de 100 reais;')
    n50 = resto // 50
    resto = resto % 50
    print(f'{n50} notas de 50 reais;')
    n10 = resto // 10
    resto = resto % 10
    print(f'{n10} notas de 10 reais;')
    n5 = resto // 5
    resto = resto % 5
    print(f'{n5} notas de 5 reais;')
    print(f'{resto} notas de 1 real.')
else:
    print("Valor inválido.")
	
/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


q1 = input('Telefonou para a vítima? s/n: ')
q2 = input('Esteve no local do crime? s/n: ')
q3 = input('Mora perto da vítima? s/n: ')
q4 = input('Devia para a vítima? s/n: ')
q5 = input('Já trabalhou com a vítima? s/n: ')
perguntas = [q1, q2, q3, q4, q5]
num = 0

for i in range(0, 5):
    if perguntas[i] == 's':
        num += 1
print(num)

if num==2:
    result = 'Suspeita'
elif num==3 or num==4:
    result = 'Cúmplice'
elif num==5:
    result = 'Assassino'
else: result = 'Inocente'
        
print(result)

/*-----------------------------------------------------------------------------------------------------*/
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg Acima de 5 Kg
Morango 2,50 por Kg 2,20 por Kg
Maçã 1,80 por Kg 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
/*-----------------------------------------------------------------------------------------------------*/

qtdMorango = float(input('Digite a quantidade em KG de morangos: '))
qtdMaca = float(input('Digite a quantidade em KG de maçãs: '))


if qtdMorango <= 5:
    valMorango = 2.5 * qtdMorango
else:
    valMorango = 2.2 * qtdMorango

if qtdMaca <= 5:
    valMaca = 1.8 * qtdMaca
else:
    valMaca = 1.5 * qtdMaca

total = valMaca + valMorango

if qtdMorango + qtdMaca > 8 or total > 25:
    total = total - (total * 0.1)

print(f'Valor final: {total}')

/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    entrada = float(input('Digite um valor entre 0 e 10: '))    
    if entrada < 0 or entrada > 10:    
        print('Valor inválido. \nDigite um valor válido!')
    else:
        break
		
/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que leia e valide as seguintes informações: Nome: maior que 3 caracteres; Idade: entre 0 e 150; Salário: maior que zero; Sexo: 'f' ou 'm'; Estado Civil: 's', 'c', 'v', 'd';

nome = ''
idade = -1
salario = 0
sexo = ''
estadoCivil = ''

while len(nome) <= 3:
    nome = input('Digite um nome com mais de 3 caracteres: ')
else:
    while idade < 0 or idade > 150:
        idade = int(input('Digite uma idade entre 0 e 150 anos: '))
    else:
        while salario <= 0:
            salario = float(input('Digite um salário maior que 0: '))
        else:
            while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd': 
                estadoCivil = input('Digite o estado civil (s/c/v/d): ')
            else:
                print(f'Nome: {nome} \nIdade: {idade} \nSalário: {salario} \nEstado Civil: {estadoCivil}')
				
/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que leia 5 números e informe o maior número.

lista = []
i = 0

while i < 5:
    num = int(input('Digite um número: '))
    lista.append(num)
    i += 1
else:
    print(max(lista))
	
/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
soma = 0
i = 0

while i < 5:
    num = int(input('Digite um número: '))
    lista.append(num)
    i += 1
else:
    i = 0
    while i < 5:
        soma += lista[i]
        i += 1
    else:
        print(f'Soma: {soma} \nMédia: {soma/len(lista)}')
		
/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for num in range(0,50):
    if num%2 != 0:
        print(num)
		
/*-----------------------------------------------------------------------------------------------------*/
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
5 X 10 = 50

num = int(input('Digite um número inteiro de 1 a 10: '))

for i in range(1,11):
  r = num*i
  print(f'{num} X {i} = {r}\n')
  

/*-----------------------------------------------------------------------------------------------------*/
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.

num = int(input('Digite o n-ésimo termo: '))
a = 0
b = 1

for i in range(0, num):
    print(b)
    aux = b
    b = a + b
    a = aux
	
	
/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('Digite um número: '))

for i in range(1, num):
    num = num*i
print(num)

/*-----------------------------------------------------------------------------------------------------*/
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
50 - R$ 99.50
valor = 1.99

print('Loja Quase Dois - Tabela de Preços')
for i in range(1, 51):
  print(f'{i} - R${valor:.2f}')
  valor += 1.99
  
/*-----------------------------------------------------------------------------------------------------*/
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
50 - R$ 9.00


valor = float(input('Digite o preço do pão: '))
valorb = valor

print(f'Preço do pão: R${valor} \nPanificadora Pão de Ontem')
for i in range(1, 51):
  print(f'{i} - R${valor:.2f}')
  valor += valorb
  
/*-----------------------------------------------------------------------------------------------------*/
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00

print('Lojas Tabajara')
i = 1
total = 0.0

while True:
  valor = float(input(f'\nProduto {i}: R$'))
  total += valor 
  i += 1

  if valor == 0:
    print(f'\nTotal: R${total}')
    dinheiro = float(input('\nDinheiro: R$'))
    troco = dinheiro - total
    print(f'\nTroco: R${troco}\n...')
    i = 1
    total = 0.0

/*-----------------------------------------------------------------------------------------------------*/
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
-Código da cidade;
-Número de veículos de passeio (em 1999);
-Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
-Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
-Qual a média de veículos nas cinco cidades juntas;
-Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cidades = {
    "cidade0": [856, 2],
    "cidade1": [1000, 80],
    "cidade2": [921, 7],
    "cidade3": [10, 8],
    "cidade4": [342, 42]
}

menorIndice = [cidades["cidade0"][0], cidades["cidade0"][1]]
maiorIndice = [cidades["cidade0"][0], cidades["cidade0"][1]]
somaVeiculos = 0
somaAcidentes = 0
i = 0

for cid in cidades:
    somaVeiculos += cidades[cid][0]
    if cidades[cid][0] < 2000:
        somaAcidentes += cidades[cid][1]
        i += 1
    if cidades[cid][1] > maiorIndice[0]:
        maiorIndice[0] = cidades[cid][1]
        maiorIndice[1] = cid
    if cidades[cid][1] < menorIndice[0]:
        menorIndice[0] = cidades[cid][1]
        menorIndice[1] = cid
        
    
mediaVeiculos = somaVeiculos / len(cidades.keys())
mediaAcidentes = somaAcidentes / i

print("Maior índice de acidentes: ", maiorIndice)
print("Menor índice de acidentes: ", menorIndice)
print("Média de veículos nas cinco cidades juntas: ", mediaVeiculos)
print("Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: ", mediaAcidentes)

/*-----------------------------------------------------------------------------------------------------*/
24.Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
9 20
12 25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
RS 1.000,00 0 1 RS 1.000,00
RS 1.100,00 100 3 RS 366,00
RS 1.150,00 150 6 RS 191,67


divida1 = float(input('Digite o valor da dívida: '))
print('Dívida \t Valor dos Juros \t Quantidade de Parcelas \t Valor da Parcela')

for i in range(0, 5):
    if i == 0:
        juros = 0
    elif i == 1:
        juros = 10
    else:
        juros += 5

    jurosv = divida1*(juros/100)
    divida = divida1+jurosv

    if i == 0:
        parcelas = 1
    else:
        parcelas = i*3
    if parcelas != 0:
        parcelav = divida/parcelas
    else:
        parcelav = divida

    print(f'R$ {divida} \t {jurosv} \t\t\t\t\t {parcelas} \t\t\t\t\t\t R$ %.2f'%(parcelav))

/*-----------------------------------------------------------------------------------------------------*/
Faça um programa que mostre os n termos da Série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. Imprima no final a soma da série.

n = int(input('Digite a quantidade de termos: '))
S = ''
b = 1
soma = 1/1


for a in range(1,n):
  S += str(a) + '/' + str(b)

  a += 1
  b += 2
  soma += a/b

  if a != n:
    S += ' + '

print(S + f'\nSoma: {soma}')