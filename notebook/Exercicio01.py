# FIZ OS EXECERCIOS NO "VSCODE" CASO QUEIRA TIRAR OS COMENTARIOS DOS CODIGOS SELECIONE A PARTE DO CODIGO E APERTE (CTRL + ;)
# Exercicio 01
print("Bem Vindo")
print("Calcula a area do circulo")
print("Digite um Valor:")
r = float(input("> "))
pi = 3.14159
area = r**2*pi
print("A medida da area é:", area)

# OU

# Exercicio 01
raio = float(input("Informe o valor do raio: "))
pi = 3.14
area = raio**2*pi
print ("A area do circulo de raio", area)
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# Exercicio 02
lad = float(input('Digite o lado do quadrado: '))
aq = lad * lad
aqd = aq * 2
print('A área do quadrado é',aq,'e o dobro desta área é',aqd)
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# Exercicio 03
qh = float(input('Quanto ganha por hora?'))
qm = int(input('Qual o numero de horas trabalhadas no mês?'))
ts = qh * qm
print('Seu salario é de R$',ts)
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# Exercicio 04
far = float(input('Informe a temperatura em graus farenheit:'))
cer= (5 * (far-32) / 9)
print('A temperatura em graus Celsius é ',cer,'°C')
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# Exercicio 05
gc = float(input('Digite uma temperatura em graus Celsius:'))
gf = gc * (9 / 5) + 32
print('A temperatura em graus Farenheit é:',gf,'°F')
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# -- Exercicio 06
nint1 = int(input('Digite um número inteiro:'))
nint2 = int(input('Digite outro número inteiro:'))
nr = float(input('Digite um número real:'))

# o produto do dobro do primeiro com metade do segundo.
e1 = nint1 * 2 * (nint2 / 2)
print('O produto do dobro do primeiro número com metade do segundo número digitado é =',e1)

# a soma do triplo do primeiro com o terceiro.
e2 = nint1 * 3 + nr
print('A soma do triplo do primeiro número com o terceiro número digitado é =',e2)

# o terceiro elevado ao cubo.
e3 = nr ** 3
print('O terceiro número digitado elevado ao cubo é =',e3)
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
Exercicio 7
p = float(input('Digite o número de quilos do peixe que você pegou:'))
if p > 50:
    multa = (p - 50) * 4
    print('Total da multa:R$',multa)
else:
    print('Não teve excesso')
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
Exercicio 8
qh = float(input('Quanto você ganha por hora:'))
h = int(input('Número de horas trabalhadas no mês:'))

sb = qh * h
print('Seu salário bruto é',sb)

inss = (8/100.0) * sb
print('INSS =',inss)

sindicato = (5/100.0) * sb
print('Sindicato =',sindicato)

ir = (11/100.0) * sb
print('Imposto de Renda =',ir)

sl = sb - (inss + sindicato + ir)
print('Seu salário liquido é',sl)
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
Exercicio 9
s1 = input("String 1:")
s2 = input("String 2:")

print("Tamanho de",s1,":",len(s1))

print("Tamanho de",s2,":",len(s2))

if len(s1) == len(s2):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

if s1.lower() == s2.lower():
    print("As duas strings possuem conteúdo iguais.")
else: 
    print("As duas strings possuem conteúdo diferente.")
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
Exercicio 10
nome = input('Usuário, digite seu nome:')
nome = nome.upper()
print('O nome do usuário de trás para frente utilizando somente letras maiúsculas:',nome[::-1])
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
Exercicio 11
data = input("Digite a data da seguinte forma (dd/mm/aaaa) ")
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
print ('Você nasce em ')
print (data.split("/")[0],"de",meses[(int(data.split("/")[1])-1)],"de",data.split("/")[2])
# ----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# Exercicio 12
 leet = {
    'A': '4',
    'B': '13',
    'C': '<',
    'D': '[)',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': 'u|',
    'K': '|<',
    'L': '|_',
    'M': '^^',
    'N': '|V',
    'O': '0',
    'P': '|D',
    'Q': '9',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': '\_/',
    'V': '\\//',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '7_'
}
t = input('Escreva um texto:')
print('Texto traduzido para a grafia leet speak:')
for i in t.upper():
    if i.isalpha():
        print(leet[i]),
    else:
        print(' ')
